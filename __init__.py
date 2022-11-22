# GUI for Numerical Predictions on Graviton3 
# Copyright (c) Odycloud.

import sys
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre')
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre/GUI')

def classFactory(iface):
    """Load QGISPlugin class.
    """
    from mainPlugin import QGISPlugin  
    title = iface.mainWindow().windowTitle()
    new_title = title.replace('QGIS', 'GUI for Numerical Predictions in the public cloud (Graviton3)')
    iface.mainWindow().setWindowTitle(new_title)
# menus    
    vector_menu = iface.vectorMenu()
    raster_menu = iface.rasterMenu()
#    mesh_menu = iface.meshMenu()
    database_menu = iface.databaseMenu()
    web_menu = iface.webMenu()
#    processing_menu = iface.processingMenu()
    menubar = vector_menu.parentWidget()
    menubar.removeAction(vector_menu.menuAction())
    menubar.removeAction(raster_menu.menuAction())
    menubar.removeAction(database_menu.menuAction())
#    menubar.removeAction(mesh_menu.menuAction())
    menubar.removeAction(web_menu.menuAction())
#    menubar.removeAction(processing_menu.menuAction())
#    menubar.addAction(dummy_menu)
    return QGISPlugin(iface)

