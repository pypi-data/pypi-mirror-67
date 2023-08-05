import numpy as np
import pyqtgraph.opengl as gl
from PyQt5 import QtCore, QtGui
from .gltextitem import GLTextItem

class LidarGraphicsView(gl.GLViewWidget):
    threePointsPicked = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        # init the widget
        super().__init__(parent)

        # Main cloud data
        self.rawPoints = np.zeros((1,3))
        self.rawColor = np.zeros((1,3), dtype=np.float32)
        self.rawPtSize = 4
        self.rawCloud = gl.GLScatterPlotItem(
            pos=self.rawPoints,color=self.rawColor,size=self.rawPtSize)
        self.addItem(self.rawCloud)

        # background cloud
        self.bgPoints = np.zeros((1,3))
        self.bgColor = (0.0, 0.0, 1.0, 0.0)
        self.bgPtSize = 2
        self.bgCloud = gl.GLScatterPlotItem(
            pos=self.bgPoints,color=self.bgColor,size=self.bgPtSize)
        self.addItem(self.bgCloud)

        # crop box outline, top polygon, bottom polygon, connections, node names
        self.cb_size = 2
        self.cbColor = np.zeros((2,3), dtype=np.float32)
        self.cb_range = []
        self.connections = []
        self.box_points_id = []

        self.cb_top_poly = np.zeros((2,3))
        self.cb_top_poly_line = gl.GLLinePlotItem(pos=self.cb_top_poly,
            color=self.cbColor, width=self.cb_size)
        self.addItem(self.cb_top_poly_line)

        self.cb_bottom_poly = np.zeros((2,3))
        self.cb_bottom_poly_line = gl.GLLinePlotItem(pos=self.cb_bottom_poly,
            color=self.cbColor, width=self.cb_size)
        self.addItem(self.cb_bottom_poly_line)

        # cluster box
        self.cluster_box_lines = []
        self.cluster_box_text = []
        self.box_color = (1.0, 1.0, 0.0, 1.0)
        self.box_width = 2
        self.cluster_boxes = []
        self.cluster_labels = []
        self.box_mesh_faces = np.array([
                [0, 1, 3],
                [1, 2, 3],
                [4, 5, 7],
                [5, 6, 7],
                [0, 1, 4],
                [1, 5, 4],
                [1, 2, 6],
                [2, 6, 5],
                [3, 0, 4],
                [0, 4, 7],
                [2, 3, 7],
                [3, 7, 6]
            ])
        self.box_mesh_colors = np.tile(np.array([1.0, 1.0, 0.0, 0.3]),
            (self.box_mesh_faces.shape[0], 1))
        self.box_mesh_vcolors = np.tile(np.array([1.0, 1.0, 0.0, 0.3]),
            (8, 1))

        # setup grid
        self.grid = gl.GLGridItem()
        self.grid.scale(1,1,1)
        self.addItem(self.grid)

        # axes and annotation
        self.axes = gl.GLAxisItem(glOptions="additive")
        self.addItem(self.axes)
        xax = GLTextItem(X=1, Y=0, Z=0, text="X")
        yax = GLTextItem(X=0, Y=1, Z=0, text="Y")
        zax = GLTextItem(X=0, Y=0, Z=1, text="Z")
        self.addItem(xax)
        self.addItem(yax)
        self.addItem(zax)

        # points selection
        self.clickRadius = 5
        self.selectionAllowed = False
        self.nSelected = 0
        self.selected = np.zeros((3,3))
        self.selectedVisible = True

        self.selectedSize = 10
        self.selectedScatter = gl.GLScatterPlotItem(pos=np.zeros((1,3)),
            color=(1.0, 0.0, 0.0, 0.0),size=self.selectedSize)
        self.addItem(self.selectedScatter)
        self.triangleWidth = 5
        self.triangle = gl.GLLinePlotItem(pos=np.zeros((2,3)),
            color=(1.0, 0.0, 1.0, 0.0), width=self.triangleWidth)
        self.addItem(self.triangle)

    def mouseReleaseEvent(self, event):
        # proceed normally
        super().mouseReleaseEvent(event)

        # do extra if left click
        if event.button() == 2:
            if self.selectionAllowed:
                self.updateSelectedRawPoints()
                self.drawSelected()
                if self.nSelected == 3:
                    self.threePointsPicked.emit()

    def setSelectedVisible(self, state):
        self.selectedVisible = state
        self.drawSelected()
        
    def setSelectionAllowed(self, flag):
        self.selectionAllowed = flag

    def resetSelected(self):
        self.nSelected = 0
        self.drawSelected()

    def getSelectedPoints(self):
        return self.selected

    def drawSelected(self):
        if self.nSelected == 0 or not self.selectedVisible:
            self.selectedScatter.setData(pos=np.zeros((1,3)),
                color=(1.0, 0.0, 0.0, 0.0),size=self.selectedSize)
            self.triangle.setData(pos=np.zeros((2,3)),
            color=(1.0, 0.0, 1.0, 0.0),width=self.triangleWidth)
        else:
            self.selectedScatter.setData(pos=self.selected[:self.nSelected,:],
                color=(1.0, 0.0, 0.0, 1.0), size=self.selectedSize)
            if self.nSelected > 1:
                edges = self.selected[:self.nSelected,:]
                color = (1.0, 0.0, 1.0, 1.0)
                if self.nSelected == 3:
                    edges = np.vstack((self.selected, self.selected[0,:]))
                    color = (1.0, 1.0, 0.0, 1.0)
                self.triangle.setData(pos=edges,color=color,width=self.triangleWidth)

    def updateSelectedRawPoints(self):
        m = self.projectionMatrix() * self.viewMatrix()
        view_w = self.width()
        view_h = self.height()
        mouse_x = self.mousePos.x()
        mouse_y = self.mousePos.y()

        # project all raw points to 2d screen plane, calculate distance from clicked mouse
        distances = []
        # TODO:rewrite in numpy way without loops!
        for pt in self.rawPoints: 
            projected_pt = m.map(QtGui.QVector3D(pt[0],pt[1],pt[2]))
            x_pixel = view_w * (projected_pt.x() + 1)/2
            y_pixel = view_h * (- projected_pt.y() + 1)/2
            d = np.linalg.norm(np.array([mouse_x, mouse_y])-np.array([x_pixel, y_pixel]))
            distances.append(d)
        
        # find closest, update
        idx = np.nanargmin(distances)
        if self.nSelected == 3:
            self.nSelected = 0
        elif distances[idx] > self.clickRadius:
            return
        else:
            self.selected[self.nSelected] = self.rawPoints[idx]
            self.nSelected += 1

    def setBackgroundPoints(self, pts):
        if pts is None:
            self.bgPoints = np.zeros((1,3))
            self.bgColor = (0.0, 0.0, 1.0, 0.0)
        else:
            self.bgPoints = pts
            self.bgColor = (0.0, 0.0, 1.0, 1.0)

    def setRawPoints(self, pts):
        if pts is None:
            self.rawPoints = np.zeros((1,3))
            self.rawColor = np.zeros((1,3), dtype=np.float32)
        else:
            self.rawPoints = pts
            self.rawColor = np.zeros((pts.shape[0],3), dtype=np.float32)
            self.rawColor[:,0] = 0
            self.rawColor[:,1] = 1
            self.rawColor[:,2] = 0

    def setCropBox(self, polygon, zrange):
        if polygon is None or len(polygon) < 3:
            self.cb_top_poly = np.zeros((2,3))
            self.cb_bottom_poly = np.zeros((2,3))
            self.cbColor = np.zeros((2,3), dtype=np.float32)
        else:
            polygon = np.array(polygon)
            n_rows = polygon.shape[0]
            self.cb_range = zrange
            self.cb_top_poly = np.hstack((polygon, zrange[1] * np.ones((n_rows,1))))
            self.cb_top_poly = np.vstack((self.cb_top_poly, self.cb_top_poly[0,:]))
            self.cb_bottom_poly = np.hstack((polygon, zrange[0] * np.ones((n_rows,1))))
            self.cb_bottom_poly = np.vstack((self.cb_bottom_poly, self.cb_bottom_poly[0,:]))
            self.cbColor = (1.0, 0.0, 0.0, 1.0)

    def setClusterAABB(self, polygons):
        self.cluster_boxes = []
        if polygons:
            for p in polygons:
                self.cluster_boxes.append(p)

    def setClusterLabels(self, labels):
        self.cluster_labels = []
        if labels:
            for l in labels:
                self.cluster_labels.append(l)

    def draw(self):
        #draw raw points
        self.rawCloud.setData(pos=self.rawPoints,
            color=self.rawColor,size=self.rawPtSize)
        
        #bg
        self.bgCloud.setData(pos=self.bgPoints,
            color=self.bgColor,size=self.bgPtSize)
        
        # draw crop box
        self.drawCropBox()

        # draw clusters
        self.drawClusters()

    def drawCropBox(self):
        self.cb_top_poly_line.setData(pos=self.cb_top_poly,
            color=self.cbColor, width=self.cb_size)
        self.cb_bottom_poly_line.setData(pos=self.cb_bottom_poly,
            color=self.cbColor, width=self.cb_size)

        # remove ocnnections
        try:
           [self.removeItem(c) for c in self.connections]
        except Exception:
            pass
        
        # remove text
        try:
            [self.removeItem(t) for t in self.box_points_id]
        except Exception:
            pass

        if self.cb_top_poly.shape[0] > 2:
            # create new connections
            self.connections = []
            self.box_points_id = []
            for i in range(self.cb_top_poly.shape[0] - 1):
                pts = np.vstack((self.cb_bottom_poly[i,:], self.cb_top_poly[i,:]))

                # add connection line
                con_line = gl.GLLinePlotItem(pos=pts,
                    color=self.cbColor, width=self.cb_size)
                self.connections.append(con_line)
                self.addItem(con_line)

                #add text
                t = GLTextItem(X=pts[1,0], Y=pts[1,1], Z=pts[1,2], text=f"p{i+1}")
                self.box_points_id.append(t)
                self.addItem(t)

    def drawClusters(self):
        # cluster boxes
        try:
            [self.removeItem(b) for b in self.cluster_box_lines]
        except Exception:
            pass

        # remove text
        try:
            [self.removeItem(t) for t in self.cluster_box_text]
        except Exception:
            pass

        self.cluster_box_lines = []
        self.cluster_box_text = []
        for box, label in zip(self.cluster_boxes, self.cluster_labels):
            l = gl.GLLinePlotItem(pos=box, color=self.box_color,
                width=self.box_width)
            self.addItem(l)
            self.cluster_box_lines.append(l)

            #add cluster labels
            cx, cy = np.mean(box[0:4,0:2],axis=0)
            z = np.max(box[:,2])
            t = GLTextItem(X=cx, Y=cy, Z=z,
                text="ID_{}".format(label))
            self.addItem(t)
            self.cluster_box_text.append(t)

if __name__ == "__main__":
    from PyQt5 import QtWidgets, QtCore
    import sys
    # demo
    app = QtWidgets.QApplication(sys.argv)
    mainView = QtWidgets.QMainWindow()
    mainView.setWindowTitle("Demo main window")
    mainView.resize(800, 600)
    centralWidget = QtWidgets.QWidget()
    centralWidget.setMinimumSize(QtCore.QSize(400, 300))
    mainLayout = QtWidgets.QVBoxLayout(centralWidget)
    mainView.setCentralWidget(centralWidget)

    graphicsView = LidarGraphicsView()
    mainLayout.addWidget(graphicsView)
    
    pts = -0.5 + np.random.rand(500,3)
    graphicsView.setRawPoints(pts)

    poly = np.array([
        [-0.5, -0.5],
        [0.5, -0.5],
        [0.5, 0.0],
        [-0.5, 0.0]
        ])
    graphicsView.setCropBox(polygon=poly, zrange=[-0.5, 0.5])
    graphicsView.draw()
    mainView.show()
    sys.exit(app.exec())
