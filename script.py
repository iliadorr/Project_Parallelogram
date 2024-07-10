from utils.load_file import load_data
from utils.get_figures_number import *
from utils.get_alpha import *
from utils.get_beta import *
from utils.get_gamma import *
from utils.get_surface_area import *
from utils.get_volume import *
from utils.get_radius_described_sphere import *
from utils.get_volume_described_sphere import *
from utils.get_diag import *
from utils.characs import *
from utils.write_file import *
from utils.printing_first import *

#start of program
print('Project Paralellogram is started! ')
print(get_printing_first())

fig_dic = {} #dictionary of read file
fig_num = 0 #figures number in dict file


fig_dic = load_data('parallelepipeds.json') #load json dictionary from file
fig_num = get_figures_number(fig_dic)

	#print(fig_num) #print number of figures!
	#print(fig_sides[0][1])

characteristics = get_characs(fig_dic) #Making dictionary.
	#print(characteristics)

print(set_write_file(characteristics)) #wrtie calculated json to file.

#end of program
print('End of program')