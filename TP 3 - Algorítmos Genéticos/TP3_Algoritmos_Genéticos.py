import random
import time

colores = ['roja', 'azul', 'verde', 'blanca', 'amarilla']
profesiones = ['Matematico', 'Hacker', 'Ingeniero', 'Analista', 'Desarrollador']
lenguajes = ['Python', 'C#', 'Java', 'C++', 'Javascript']
db = ['Cassandra', 'MongoDB', 'HBase', 'Neo4j', 'Redis']
editores = ['Brackets', 'Sublime Text', 'Vim', 'Atom', 'Notepad++']

genes = [colores, profesiones, lenguajes, db, editores]
tamano_gen = len(genes)

class Fenotipo:
    def __init__(self):
        self.cromosoma = [[0] * tamano_gen for _ in range(tamano_gen)]
        self.puntaje = 20
        self.aprobado = 0

    def get_gene(self, x, y):
        return self.cromosoma[x][y]

    def generar_individuo(self):
        for x in range(tamano_gen):
            for y in range(tamano_gen):
                self.cromosoma[x][y] = random.choice(genes[x])

    def mutacion(self, probabilidad_mutacion=0.8):
        for fila in self.cromosoma:
            for j in range(tamano_gen):
                if random.random() < probabilidad_mutacion:
                    fila[j] = random.choice(genes[self.cromosoma.index(fila)])

    def aptitud(self):
        self.aprobado = 0
        self.puntaje = 20
        puntaje_fallido = 0.5
        puntaje_penalidad = 1

        for x in range(0, tamano_gen):
            if len(set(self.cromosoma[x])) != len(self.cromosoma[x]):
                self.puntaje -= puntaje_penalidad * 2

        if all(len(set(column)) == tamano_gen for column in zip(*self.cromosoma)):
            self.aprobado += 1

        try:
            i = self.cromosoma[1].index('Matematico')
            if self.cromosoma[0][i] == 'roja':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[1].index('Hacker')
            if self.cromosoma[2][i] == 'Python':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[0].index('verde')
            if self.cromosoma[4][i] == 'Brackets':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[1].index('Analista')
            if self.cromosoma[4][i] == 'Atom':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[0].index('verde')
            if self.cromosoma[0][i-1] == 'blanca':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[3].index('Redis')
            if self.cromosoma[2][i] == 'Java':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[0].index('amarilla')
            if self.cromosoma[3][i] == 'Cassandra':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            if self.cromosoma[4][2] == 'Notepad++':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            if self.cromosoma[1][0] == 'Hacker':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[3].index('HBase')
            if i == 0:
                if self.cromosoma[2][i+1] == 'Javascript':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
            elif i == 4:
                if self.cromosoma[2][i-1] == 'Javascript':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
            else:
                if self.cromosoma[2][i+1] == 'Javascript' or self.cromosoma[2][i-1] == 'Javascript':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[3].index('Cassandra')
            if i==0:
                if self.cromosoma[2][i+1] == 'C#':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
            elif i==4:
                if self.cromosoma[2][i-1] == 'C#':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
            else:
                if self.cromosoma[2][i+1] == 'C#' or self.cromosoma[2][i-1] == 'C#':
                    self.puntaje += 1
                    self.aprobado += 1
                else:
                    self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[3].index('Neo4j')
            if self.cromosoma[4][i] == 'Sublime Text':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[1].index('Ingeniero')
            if self.cromosoma[3][i] == 'MongoDB':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad

        try:
            i = self.cromosoma[1].index('Hacker')
            if self.cromosoma[0][i] == 'azul':
                self.puntaje += 1
                self.aprobado += 1
            else:
                self.puntaje -= puntaje_fallido
        except (ValueError, IndexError):
            self.puntaje -= puntaje_penalidad


class Adivinanza:
    def __init__(self):
        self.poblacion = []

    def resolver(self, cant_poblacion):
        self.generar_poblacion(cant_poblacion)

        individuo, fit = self.iterar(cant_poblacion)

        print("¿Quien usa Vim?")
        indices = [i for i, x in enumerate(individuo[4]) if x == "Vim"]
        if indices:
            for index in indices:
                print(f"El individuo que vive en la casa {individuo[0][index]}, que es {individuo[1][index]}, que programa en {individuo[2][index]} y usa la base de datos {individuo[3][index]} usa Vim")
        else:
            print("Nadie usa Vim")
            
    def mutacion(self, cant_poblacion, mutaciones=200):
        random_numbers = [x for x in range(0, cant_poblacion)]
        random.shuffle(random_numbers)
        del random_numbers[mutaciones:]
        for i in random_numbers:
            self.poblacion[i].mutacion()


    def generar_poblacion(self, population_size):
        for _ in range(population_size):
            nuevo_hijo = Fenotipo()
            nuevo_hijo.generar_individuo()
            self.poblacion.append(nuevo_hijo)


    def crossover(self, cant_poblacion, liveness=100, liveness_prob=0.80):
        poblacion_buena = []
        i = 0
        while len(poblacion_buena) < liveness:
            if random.random() < liveness_prob:
                poblacion_buena.append(self.poblacion[i])
            i += 1
            i %= len(self.poblacion)

        offspring = []
        while len(offspring) <= cant_poblacion:
            primero, segundo = random.sample([x for x in range(0, len(poblacion_buena) - 1)], k=2)
            segundo = random.randint(len(poblacion_buena), cant_poblacion - 1)
            nuevo_hijo = self.cruzar(poblacion_buena[primero], self.poblacion[segundo])
            offspring.append(nuevo_hijo)

        self.poblacion = offspring


    def cruzar(self, padre_1, padre_2):
        nuevo_hijo = Fenotipo()
        for x in range(tamano_gen):
            for y in range(tamano_gen):
                i = random.randint(0,1)
                if i == 0:
                    nuevo_hijo.cromosoma[x][y] = padre_1.get_gene(x,y)
                else:
                    nuevo_hijo.cromosoma[x][y] = padre_2.get_gene(x,y)
        return nuevo_hijo


    def iterar(self, cant_poblacion):
        contador = 0
        repetidos = 0
        mejor_anterior = Fenotipo().cromosoma
        while True:
            # Seleccion
            for x in range(len(self.poblacion)):
                self.poblacion[x].aptitud()
            self.poblacion.sort(key=lambda x: x.puntaje, reverse=True)

            contador += 1
            if contador % 10 == 0:
                print("--------------------------------")
                print(f"Iteracion: {contador}")
                print(f"Repetidos: {repetidos}")
                print(f"Individuo: {self.poblacion[0].cromosoma}")
                print(f"Fit: {self.poblacion[0].aprobado}")
                print(f"puntaje: {self.poblacion[0].puntaje}")

            if self.poblacion[0].cromosoma == mejor_anterior:
                repetidos += 1
            else:
                repetidos = 0
            mejor_anterior = self.poblacion[0].cromosoma

            aprobado =  self.poblacion[0].aprobado
            if aprobado >= 15:
                break

            if repetidos == 50:
                print("Mutando...")
                repetidos = 0
                self.mutacion(cant_poblacion, mutaciones=cant_poblacion)
                continue

            self.crossover(cant_poblacion)

            self.mutacion(cant_poblacion)

        return self.poblacion[0].cromosoma, self.poblacion[0].aprobado


start = time.time()

riddle = Adivinanza()
riddle.resolver(cant_poblacion = 1000)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))