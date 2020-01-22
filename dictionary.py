### This is the dictionary containing the characteristics of each color and shape ###

# class Object_Dictionary:
#     def __init__(self):
#         pass

    # def color_ranges(self):
        colors = {
                'HSV':
                    {
                    'red':([161, 155, 100], [179, 255, 255]),
                    'orange':([11, 153, 214], [25, 255, 255]),
                    'blue':([94, 80, 2], [126, 255, 255]),
                    'green':([25, 52, 72], [102, 255, 255]), #green picks up light blue
                    }
                'RGB': 
                    {
                    'red':([10, 10, 120], [104, 104, 255]),
                    'orange':([0, 100, 200], [104, 175, 255])
                    }
                }
        
    #     print (colors)
    #     print (red)

        

colors = {
        'RGB': 
            {
            'red':([10, 10, 120], [104, 104, 255]),
            'orange':([0, 100, 200], [104, 175, 255])
            }
        }

print(colors)
print(colors['RGB']['red'])

