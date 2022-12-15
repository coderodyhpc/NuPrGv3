# GUI for Numerical Predictions on Graviton3 
# Copyright (c) Odycloud.

import sys
import subprocess
from qgis.core import QgsCoordinateReferenceSystem, QgsProject
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolBar, QPushButton
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre')
sys.path.insert(1,'/opt/.Odycloud/Ody_NumPre/GUI')

def classFactory(iface):
    """Load QGISPlugin class.
    """
    from mainPlugin import QGISPlugin  
    QgsProject.instance().title = 'MODELING'
    titulus = QgsProject.instance().title() 
    title = iface.mainWindow().windowTitle()
    new_title = title.replace('QGIS', 'Gv3 Graphical Interface')
    iface.mainWindow().setWindowTitle(new_title)

    odyicon = QIcon("/opt/.Odycloud/Ody_NumPre/iconlightgray32.png")
    iface.mainWindow().setWindowIcon(odyicon)

    iface.mainWindow().statusBar().setFont(QFont('Verdana', 10))  
    iface.mainWindow().statusBar().setStyleSheet("background-color:#4B555C; color: white;")  
    command1 = ['ec2metadata', '--instance-id']
    proc1 = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_INSTANCE_IDx = proc1.communicate()[0].decode("utf-8")
    EC2_INSTANCE_ID = EC2_INSTANCE_IDx.strip() 
    command2 = ['ec2metadata', '--instance-type']
    proc2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_INSTANCE_TYPEx = proc2.communicate()[0].decode("utf-8")
    EC2_INSTANCE_TYPE = EC2_INSTANCE_TYPEx.strip() 
    command3 = ['ec2metadata', '--availability-zone']
    proc3 = subprocess.Popen(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    EC2_ZONEx = proc3.communicate()[0].decode("utf-8")
    EC2_ZONE = EC2_ZONEx.strip() 
    
    lscpu_nomen = ((subprocess.check_output("lscpu", shell=True).strip()).decode())
    for item in lscpu_nomen.split("\n"):
        if "Model name" in item:
            modeln_1 = item.strip()
    modeln_2 = modeln_1.replace("Model name:","")    
    cpu_nomen = modeln_2.replace(" ","")  
    if cpu_nomen == 'Neoverse-N1':
        nomen2 = "Graviton2"
    elif cpu_nomen == '1':
        nomen2 = "Graviton3"
    else:    
        nomen2 = cpu-nomen
    cpu_NM = "CPU: "+nomen2+"\n"
    cpu_NM2 = EC2_INSTANCE_TYPE
#    cpu_NM2.replace("\n","")
    cpu_NM3 = EC2_ZONE
    cpu_TOTAL = cpu_NM+cpu_NM2 
    odyimum = QPushButton(cpu_TOTAL) 
    odyimum.setStyleSheet(".QPushButton {color: black; background-color:#FF9900;}")
    odyimum.setFont(QFont('Verdana', 10))
    iface.mainWindow().statusBar().addWidget(odyimum)                   
    
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

