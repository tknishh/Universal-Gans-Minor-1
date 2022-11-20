import sys
import glob
from PIL import Image

pattern = sys.argv[1]
rows = int(sys.argv[2])
cols = int(sys.argv[3])
filenames = glob.glob(pattern)

images = [Image.open(name).resize((224,224)) for name in filenames]

newImage = Image.new('RGB', (cols*224, rows*224))
