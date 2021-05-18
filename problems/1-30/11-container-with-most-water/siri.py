from typing import List


def getValue(obj):
    return obj.get('y')


class Solution:
    def maxArea(self, height: List[int]):
        height_objs = []
        for i in range(len(height)):
            temp_dict = dict([('x', i), ('y', height[i])])
            height_objs.append(temp_dict)
        height_objs.sort(key=getValue)
        longest = 0
        for i in range(len(height_objs)):
            for j in range(i, len(height_objs)):
                if height_objs[i]['y'] * \
                        abs(height_objs[j]['x'] - height_objs[i]['x']) > longest:
                    longest = height_objs[i]['y'] * \
                        abs(height_objs[j]['x'] - height_objs[i]['x'])

        return longest
