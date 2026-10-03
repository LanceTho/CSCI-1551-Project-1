from direct.showbase.ShowBase import ShowBase
import sys

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

        self.accept("escape", self.quit)

    def quit(self):
        sys.exit()

    def SetupScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        tex_u = self.loader.loadTexture("./Assets/Universe/universe.jpg")
        self.Universe.setTexture(tex_u, 1)
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p1 = self.loader.loadTexture("./Assets/Planets/uranus.jpg")
        self.Planet1.setTexture(tex_p1, 1)
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-500, 1000, 1000)
        self.Planet1.setScale(350)
        
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p2 = self.loader.loadTexture("./Assets/Planets/jupiter.jpg")
        self.Planet2.setTexture(tex_p2, 1)
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(-270, 5076, -607)
        self.Planet2.setScale(350)
        
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p3 = self.loader.loadTexture("./Assets/Planets/mars.jpg")
        self.Planet3.setTexture(tex_p3, 1)
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(350, 4020, 522)
        self.Planet3.setScale(350)
        
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p4 = self.loader.loadTexture("./Assets/Planets/neptune.jpg")
        self.Planet4.setTexture(tex_p4, 1)
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(1000, 2254, 335)
        self.Planet4.setScale(350)
        
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p5 = self.loader.loadTexture("./Assets/Planets/mercury.jpg")
        self.Planet5.setTexture(tex_p5, 1)
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(235, 3210, 721)
        self.Planet5.setScale(350)
        
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        tex_p6 = self.loader.loadTexture("./Assets/Planets/venus.jpg")
        self.Planet6.setTexture(tex_p6, 1)
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(100, 6256, -234)
        self.Planet6.setScale(350)

        self.SpaceStation = self.loader.loadModel("./Assets/SpaceStation/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(1500, 1111, 800)
        self.SpaceStation.setScale(50)

        self.SpaceShip = self.loader.loadModel("./Assets/Spaceships/Dumbledore.x")
        self.SpaceShip.reparentTo(self.render)
        self.SpaceShip.setPos(0, 0, 0)
        self.SpaceShip.setScale(100)

app = MyApp()
app.run()