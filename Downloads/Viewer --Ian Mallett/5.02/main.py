from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys, os, traceback
if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
from math import *
pygame.display.init()
pygame.font.init()
import gl_shader as shader_module

from config import *

bounds_x_original = list(bounds_x)

###Change around as you like to prezoom on a point (below is this release's screenshot)
##bounds_x = [0.4136968978,0.4139727058]
##bounds_y = [0.3037255751,0.3039094471]

font = pygame.font.SysFont("Times New Roman.ttf",12)

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("MandebrotGLSL - Ian Mallett - v.5.02 - 2014")
pygame.display.set_mode(screen_size,RESIZABLE|OPENGL|DOUBLEBUF)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

mandelbrot_shader = shader_module.Program([
    shader_module.ShaderFragment(str(int(use_double_precision)) +
                                +str(iterations)+str(antialias) +
                                +str(1.0/smooth_shading_scale) +
                                +str(int(not use_smooth_shading)))
])
##mandelbrot_shader.save("dump.txt")

def get_input():
    global bounds_x, bounds_y
    keys_pressed = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    mouse_rel = pygame.mouse.get_rel()
    for event in pygame.event.get():
        if   event.type == QUIT: return False
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE: return False
            elif event.key == K_s and (keys_pressed[K_LCTRL] or keys_pressed[K_RCTRL]):
                #The way PyOpenGL handles data readback is somewhat complicated--and I haven't had time to understand
                #   all its nuances fully.  See this thread:
                #       http://sourceforge.net/p/pyopengl/mailman/message/31113979/
                #Unfortunately, I can't offer much since I'm not sure exactly how one's environment affects the type of
                #   the return value here--let alone what is "supposed" to happen.  Therefore, I have put down two
                #   implementations of the conversion.  Each has worked under certain ill-defined conditions.  Please
                #   check which version works for you, and if you know what's *actually supposed* to happen, let me know!
                r = glReadPixels(0,0,screen_size[0],screen_size[1],   GL_RED, GL_UNSIGNED_BYTE)
                g = glReadPixels(0,0,screen_size[0],screen_size[1], GL_GREEN, GL_UNSIGNED_BYTE)
                b = glReadPixels(0,0,screen_size[0],screen_size[1],  GL_BLUE, GL_UNSIGNED_BYTE)
                image = pygame.Surface(screen_size)
                try:
                    #   Begin string code
                    i = 0
                    for y in range(screen_size[1]):
                        for x in range(screen_size[0]):
                            color = ( ord(r[i]), ord(g[i]), ord(b[i]) )
                            image.set_at((x,screen_size[1]-y-1),color)
                            i += 1
                    #   Begin NumPy code?
##                    image = pygame.Surface(screen_size)
##                    for y in range(screen_size[1]):
##                        for x in range(screen_size[0]):
##                            image.set_at((x,screen_size[1]-y-1),(r[y][x],g[y][x],b[y][x]))
                    #   End conditional codeblocks
                except:
                    traceback.print_exc()
                    print("#### User: please see source file for comment! ####")
                pygame.image.save(image,"screenshot.png")
        elif event.type == VIDEORESIZE:
            screen_size[0] = event.w
            screen_size[1] = event.h
            
    zoom_conv = 0.0
    if mouse_buttons[0]:
        zoom_conv = zoom_scalar
    if mouse_buttons[2]:
        zoom_conv = 1.0 / zoom_scalar
    if zoom_conv != 0.0:
        center = [
            float(               mouse_position[0])/float(screen_size[0]) * (bounds_x[1]-bounds_x[0]) + bounds_x[0],
            float(screen_size[1]-mouse_position[1])/float(screen_size[1]) * (bounds_y[1]-bounds_y[0]) + bounds_y[0]
        ]
        
        bounds_x[0] = bounds_x[0]*zoom_conv + center[0]*(1.0-zoom_conv)
        bounds_x[1] = bounds_x[1]*zoom_conv + center[0]*(1.0-zoom_conv)

        bounds_y[0] = bounds_y[0]*zoom_conv + center[1]*(1.0-zoom_conv)
        bounds_y[1] = bounds_y[1]*zoom_conv + center[1]*(1.0-zoom_conv)
        
    return True
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glViewport(0,0,screen_size[0],screen_size[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,screen_size[0],0,screen_size[1])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    shader_module.Program.use(mandelbrot_shader)
    mandelbrot_shader.pass_vec2("bounds_x",bounds_x)
    mandelbrot_shader.pass_vec2("bounds_y",bounds_y)
    mandelbrot_shader.pass_vec2("screen_size",screen_size)

    glBegin(GL_QUADS)
    glVertex2f(             0,             0)
    glVertex2f(screen_size[0],             0)
    glVertex2f(screen_size[0],screen_size[1])
    glVertex2f(             0,screen_size[1])
    glEnd()

    shader_module.Program.use(None)

    def render_text(text):
        surface = font.render(text, True, (255,255,255,255))
        surface2 = pygame.Surface((surface.get_width()+10,13)).convert_alpha()
        surface2.fill((50,50,50,192))
        surface2.blit(surface,(5,2))
        return surface2
    def draw_text(text, pos):
        glPushMatrix()
        glRasterPos2i(pos[0],pos[1])
        glDrawPixels(text.get_width(),text.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(text,"RGBA",True))
        glPopMatrix()
    l = str(bounds_x[0])
    r = str(bounds_x[1])
    b = str(bounds_y[0])
    t = str(bounds_y[1])
    surface=render_text("( "+l+", "+t+" i )"); draw_text(surface,(               2,                    screen_size[1]-(13+2)))
    surface=render_text("( "+l+", "+b+" i )"); draw_text(surface,(               2,                                       2 ))
    surface=render_text("( "+r+", "+t+" i )"); draw_text(surface,(screen_size[0]-2-surface.get_width(),screen_size[1]-(13+2)))
    surface=render_text("( "+r+", "+b+" i )"); draw_text(surface,(screen_size[0]-2-surface.get_width(),                   2 ))

    def add_commas(string):
        string=list(string); string.reverse()
        new = []
        counter = 1
        for char in string:
           new.append(char)
           if counter == 3: new.append(",");counter = 0
           counter += 1
        new.reverse()
        newstring = ""
        for char in new: newstring += char
        if newstring.startswith(","): newstring = newstring[1:]
        return newstring
    surface = render_text("Zoom Factor: "+add_commas(str(int(round(  float(bounds_x_original[1]-bounds_x_original[0])/float(bounds_x[1]-bounds_x[0])  ))))+"x")
    draw_text(surface,(screen_size[0]-2-surface.get_width(),17))
    
    pygame.display.flip()
def main():
    global mandelbrot_shader
    clock = pygame.time.Clock()
    while True:
        if not get_input(): break
        draw()
        clock.tick(60)
    del mandelbrot_shader #delete before context is deleted
    pygame.quit()
if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
        input()
