import UnityPy, shutil
from pathlib import Path
from get_abfile_dependences import *

BASE_PATH = Path(r"D:/ArkAssets")
COPY_PATH = Path(r"D:\ArknightsMapAssets\Level_08-17_assets")
SCENE_PATH = 'scenes/obt/main/level_main_08-17/level_main_08-17.ab'

manifest_env = UnityPy.load(str(BASE_PATH / 'torappu.ab'))

shutil.copy(str(BASE_PATH / SCENE_PATH), str(COPY_PATH / SCENE_PATH.replace('/', '_')))
print('copied main scene: ' + SCENE_PATH)
for dep in get_deps(get_manifest(manifest_env), SCENE_PATH):
    shutil.copy(str(BASE_PATH / dep), str(COPY_PATH / dep.replace('/', '_')))
    print('copied dep: ' + dep)