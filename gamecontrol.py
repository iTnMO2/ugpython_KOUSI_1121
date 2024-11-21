import pygame as pg
import random,player,enemy

class GameManager():
    def __init__(self):
        self._player = player.Player()
        self._enemies = []
        self._effects = []
        self._factory = enemy.EnemyFactory()
        self.reset()
    @property
    def is_playing(self):
        return self._is_playing
    @property
    def is_cleared(self):
        return self._is_cleared
    

    def reset(self):
        self._is_playing = True
        self._is_cleared = False
        self._player.reset()
        self._enemies.clear()
        self._spawn_count = 0
        self._effects.clear()                   #これを加えると次のセッションに前セッションの爆発が残らない。
        
    def update(self):
        for e in self._effects:
            e.update()
        self._player.update()       #_spawn_count が変化しない。 -> self._spawn_count += 1
        if self._spawn_count > 15:
            self._spawn_count = 0
            self._enemies.append(self._factory.random_create)   #random_createは関数 -> random_create()
        for e in self._enemies:
            if e.is_alive == False:
                self._enemies.remove(e)
                break
            e.update()
  
            if e.rect.y >= 650:
                self._enemies.remove(e)
                
            if e.rect.colliderect(self._player.rect):
                self._enemies.remove(e)
                self._player.damage()
                self._player.hp -= 50
                if self._player.hp <= 0:
                    self._is_playing = False
                
                '''
                    b = enemy.BombEffect(e.rect,self._effects)   #綴りミス
                    self._effects.append(b)
                    self._enemies.remove(e)
                         #重複
                    if len(self._enemies) == 0:   #インデントミス
                        self._is_playing = False
                        self._is_cleared = True
                    return
                '''

    def draw(self,screen):
        for e in self._effects:
            e.draw(screen)                             #記号ミス
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
            
