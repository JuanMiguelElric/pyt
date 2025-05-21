class Televisao:
    def __init__(self):
        self.ligada = False
    
    def canal(self):
        return 3


t = Televisao()

print(t.ligada)  # False
print(t.canal()) # 3