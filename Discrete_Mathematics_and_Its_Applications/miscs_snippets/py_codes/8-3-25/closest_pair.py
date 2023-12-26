def dist(pair:list[tuple[int,int]])->float:
    assert(len(pair)==2)
    return ((pair[0][0]-pair[1][0])**2+(pair[0][1]-pair[1][1])**2)**(1/2)

# def get_y_coordinate(point:tuple[int,int]):
#     return point[1]
# def get_y_index(index_point:(int,tuple[int,int])):
#     return index_point[0]

# points with the increasing x-coordinate
def closest_pair(points:list[tuple[int,int]],points_cnt):
    """
    1. If using `first_max_with_index=closest_pair(points[0:sub_size+1],sub_size+1)
    second_max_with_index=closest_pair(points[sub_size:points_cnt],points_cnt-sub_size)`
    Then here if sub_size=0 -> points_cnt=1 -> 
    (last) points_cnt-sub_size=1>=(points_cnt-points_cnt/2=points_cnt/2), points_cnt=1 or 2
    OR (last) sub_size=1, i.e. points_cnt=3 or 2

    So we only needs to ensure points_cnt=3 or 2, it will not get to the weird situation points_cnt=1
    2. sub_size=0 or points_cnt-sub_size=0 -> points_cnt=0, then iteratively back from the final step,
    the original points_cnt=0, impossible.
    """
    if points_cnt==2:
        return ([(points[0],points[1])],dist(points))
    elif points_cnt==1:
        # return (points[0],points[0],0)
        print("err")
    sub_size=points_cnt//2
    split_idx=sub_size
    # points[sub_size] is the duplicate point.
    """
    1. > If any points fall on the dividing line $l$, we divide them among the two parts if necessary
    2. Here I use the same pattern as the FIGURE 1 instead of exercise 26 by `abs(elem_index[1][0]-points[sub_size][0])`
    """
    first_max_with_index=closest_pair(points[0:sub_size+1],sub_size+1)
    second_max_with_index=closest_pair(points[sub_size:points_cnt],points_cnt-sub_size)
    pnt_pair_list=[]
    first_dist=first_max_with_index[1]
    second_dist=second_max_with_index[1]
    min_dist=0
    if first_dist<second_dist:
        min_dist=first_dist
        pnt_pair_list=first_max_with_index[0]
    elif first_dist>second_dist:
        min_dist=second_dist
        pnt_pair_list=second_max_with_index[0]
    else:
        min_dist=first_dist
        pnt_pair_list=first_max_with_index[0]+second_max_with_index[0]
    middle_point_with_index_list=[(increasing_x_to_increasing_y_map[elem_index[0]],elem_index[1]) \
                                  for elem_index in enumerate(points) if abs(elem_index[1][0]-points[sub_size][0])<=min_dist]
    # https://note.nkmk.me/en/python-list-sort-sorted/#sort-a-list-using-the-sort-method
    middle_point_with_index_list=sorted(middle_point_with_index_list,key=lambda index_point:index_point[0])
    # split_line_point=points[sub_size]
    for i in range(len(middle_point_with_index_list)):
        first_pnt_cmp=middle_point_with_index_list[i][1]
        for j in range(i+1,len(middle_point_with_index_list)):
            second_pnt_cmp=middle_point_with_index_list[j][1]
            """
            Here only need one condition instead of 2 based on `abs(elem_index[1][0]-points[sub_size][0])`
            """
            # if abs(first_pnt_cmp[0]-second_pnt_cmp[0])<=2*min_dist \
            if abs(first_pnt_cmp[1]-second_pnt_cmp[1])<=min_dist:
                tmp_dist=dist([first_pnt_cmp,second_pnt_cmp])
                if tmp_dist<min_dist:
                    min_dist=tmp_dist
                    pnt_pair_list=[(first_pnt_cmp,second_pnt_cmp)]
                elif tmp_dist==min_dist:
                    if (first_pnt_cmp,second_pnt_cmp) not in pnt_pair_list \
                        and (second_pnt_cmp,first_pnt_cmp) not in pnt_pair_list :
                        pnt_pair_list+=[(first_pnt_cmp,second_pnt_cmp)]
            else:
                break
    return [pnt_pair_list,min_dist]

points_lists=[[ (1, 3), (1, 7), (2, 4), (2, 9), (3, 1), (3, 5), (4, 3), (4, 7)],\
             [(1, 2),
(1, 6), (2, 4), (2, 8), (3, 1), (3, 6), (3, 10), (4, 3), (5, 1),
(5, 5), (5, 9), (6, 7), (7, 1), (7, 4), (7, 9),(8, 6)],\
    [(1,2),(1, 6), (1, 4)]]
increasing_x_to_increasing_y_map={}
for points_list in points_lists:
    points_list=sorted(points_list,key=lambda a:a[0])
    # (3, 1),(1, 3),(4, 3),(2, 4),(3, 5),(1, 7),(4, 7),(2, 9)
    # increasing_y_points_list=[(3, 1),(1, 3),(4, 3),(2, 4),(3, 5),(1, 7),(4, 7),(2, 9)]

    increasing_y_points_list=sorted(points_list,key=lambda a:a[1])
    print(increasing_y_points_list)
    for elem_index in enumerate(points_list):
        y_index=increasing_y_points_list.index(elem_index[1])
        """
        >  but having an identification as to which points in the original list they are
        """
        increasing_x_to_increasing_y_map[elem_index[0]]=y_index
    print(closest_pair(points_list,len(points_list)),'\n')