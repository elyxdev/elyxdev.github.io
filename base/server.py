# Versiones disponibles
# forge, mohist, fabric, vanilla, paper

# Puedes instalar mohist después de instalar forge desde el menú de gestionar
# Puedes instalar paper después de instalar vanilla desde el menú de gestionar
# Puedes instalar purpur después de instalar fabric desde el menú de gestionar

# Regiones de ngrok
# Código          Lugar
#-----------      ---------------------------
# ap	          Asia / Pacífico (Singapore)
# au		      Australia (Sydney)
# eu		      Europa (Frankfurt)
# in		      India (Mumbai)
# jp		      Japón (Tokyo)
# sa		      Sudamérica (São Paulo)
# us		      Estados unidos (Ohio)
# us-cal-1	      Estados unidos (California)














# No toques nada de aquí para abajo, puedes dañarlo
import requests,os,base64,glob,time
if os.path.exists("servidor.py"):
	os.remove("servidor.py")
if not os.path.exists("./.gitignore"):
	big = "L1B5dGhvbioNCi93b3JrX2FyZWEqDQovc2Vydmlkb3JfbWluZWNyYWZ0DQovbWluZWNyYWZ0X3NlcnZlcg0KL3NlcnZpZG9yX21pbmVjcmFmdF9vbGQNCi90YWlsc2NhbGUtY3MNCi90aGFub3MNCi9zZXJ2ZXJzDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioubXNwDQoqLm91dHB1dA=="
	dec = base64.standard_b64decode(big).decode()
	with open(".gitignore", 'w') as giti:
		giti.write(dec)
def download_latest_release(download_path='.'):
	mirror = "https://elyxdev.github.io/latest"
	pet = requests.get(mirror)
	if pet.status_code == 200:
		data = pet.json()
		url = data.get('latest')
		version = url.split("/")[-1]
		if version in glob.glob("*.msp"):
			return version
		else:
			os.system("rm *.msp")
			print("Actualizando tu versión de MSP...")
			time.sleep(1.5)
		pathto = os.path.join(download_path, version)
		with open(pathto, 'wb') as archivo:
			archivo.write(requests.get(url).content)
		return version
flnm=download_latest_release()
if flnm.split(".")[-1] == "msp":
	os.system(f"chmod +x {flnm} && ./{flnm}")
else:
    os.system(f"python3 {flnm}")