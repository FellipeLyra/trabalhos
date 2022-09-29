class Moto: 
  
    def __init__(self): 
        self.nome = "Moto"
  
    def DuasRodas(self): 
        return "Duas rodas"
  
class Caminhao: 
  
    def __init__(self): 
        self.nome = "Caminhão"
  
    def OitoRodas(self): 
        return "Oito rodas"
  
class Carro: 
  
    def __init__(self): 
        self.nome = "Carro"
  
    def QuatroRodas(self): 
        return "Quatro rodas"
  
  
  
class Adapter: 
    
    def __init__(self, obj, **adapted_methods): 
      self.obj = obj 
      self.__dict__.update(adapted_methods) 
  
    def __getattr__(self, attr): 
      return getattr(self.obj, attr) 
  
    def original_dict(self): 
      return self.obj.__dict__ 
  
if __name__ == "__main__": 
  
    
    objects = [] 
  
    moto = Moto() 
    objects.append(Adapter(moto, rodas = moto.DuasRodas)) 
  
    caminhao = Caminhao() 
    objects.append(Adapter(caminhao, rodas = caminhao.OitoRodas)) 
  
    carro = Carro() 
    objects.append(Adapter(carro, rodas = carro.QuatroRodas)) 
  
    for obj in objects: 
       print("{0} tem {1} ".format(obj.nome, obj.rodas())) 
