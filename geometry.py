
"Retorna as posições dos microfones dada uma distancia e um centro
def createGeometry(C,d):
    #C->centro do triângulo
    #d->distância entre os microfones
    
    m1y = -(C[0] - d/2)
    m1x = (C[1] - np.sqrt(3)/6*d)
    
    m2y = -C[0] 
    m2x = C[1] + np.sqrt(3)/3*d
    
    m3y = -(C[0] + d/2)
    m3x = C[1] - np.sqrt(3)/6*d
    
    return ([m1x,m1y],[m2x,m2y],[m3x,m3y])

"Retorna um ponto que indentifica a posição da fonte sonora relativo a um ângulo dado
def createSourceLoc(angle):
    anglerad = math.radians(angle)
    sx = np.round(np.cos(anglerad),2)-0*np.sin(anglerad)
    sy = 0*np.cos(anglerad)+np.round(np.sin(anglerad),2)
    return ([sx,sy])

def distance(p1,p2):
    return  np.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
