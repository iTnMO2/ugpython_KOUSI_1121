import pygame as pg,sys
import gamecontrol,resultscene         #綴りミス
pg.init()
screen = pg.display.set_mode((600,650))
pg.display.set_caption("MYGAME")
game = gamecontrol.GameManager()
result = resultscene.ResultScene(game)  #綴りミス


while True:
    screen.fill(pg.Color("NAVY"))
    
    if game.is_playing == True:
        game.update()
    else:
        result.update()
    
    game.draw(screen) # # # # # # # 重複
    if game.is_playing == False:
        result.draw(screen)
        
    

    # # # 重複
    #game.draw(screen) # # # # # # # # 重複
 
    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
