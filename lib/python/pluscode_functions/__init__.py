from math import floor

# This dictionary contains the keys and values to convert pluscodes into matrice coordinates

convert_dic = {
    '2':0,
    '3':1,
    '4':2,
    '5':3,
    '6':4,
    '7':5,
    '8':6,
    '9':7,
    'C':8,
    'F':9,
    'G':10,
    'H':11,
    'J':12,
    'M':13,
    'P':14,
    'Q':15,
    'R':16,
    'V':17,
    'W':18,
    'X':19,
}

'''
    This function converts pluscodes (length must be minimum 8) into matrix coordinates.
    It takes as input the pluscode column and outputs several lists,
    containing coordinates and reduced coordiates (for a smaller matrix).'''

def convert_pluscode(pluscode_col):
    
    v_list = []
    h_list = []
    reduced_v_list = []
    reduced_h_list = []
    reduced_coordinates_list = []

    pluscode_list = pluscode_col.to_list()
    
    for code in pluscode_list:
        v = 0
        h = 0

        v += (convert_dic[code[4]]-16)*20
        h += (convert_dic[code[5]]-5)*20
        v += (convert_dic[code[6]])
        h += (convert_dic[code[7]])
        #v += (convert_dic[code[9]])
        #h += (convert_dic[code[10]])

        v_list.append(v)
        h_list.append(h)

        reduced_v_list.append(floor(v/2))
        reduced_h_list.append(floor(h/2))
        reduced_coordinates_list.append(str(floor(v/2))+','+str(floor(h/2)))
        
    return v_list, h_list, reduced_v_list, reduced_h_list, reduced_coordinates_list