
from tqdm import tqdm

cant = 10000

loop = tqdm(total = cant, position=0, leave=False)
for k in range(cant):
    loop.set_description("Cargando...".format(k))
    loop.update(1)

loop.close()