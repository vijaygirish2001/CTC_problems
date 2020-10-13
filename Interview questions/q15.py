'''

Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an
abandoned guard post while you were running through the station, so you have a chance to fight your way out. But the
beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls,
meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully).

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).


([300,275], [150,150], [185,100], 500)

'''

import math
def solution(dimensions, your_position, guard_position, distance):
    # Your code here
    def compute_dist(p1,p2):
        return math.hypot(float(p1[0]-p2[0]),float(p1[1]-p2[1]))#((float(p1[0]-p2[0]))**2 + (float(p1[1]-p2[1]))**2)**0.5

    def is_not_on_way(p1,p2, plist):
        for p in plist:
            if (p1[1] - p2[1]) == 0 or (p[1]-p2[1]) == 0:
                if (p1[1] - p2[1]) == 0 and (p[1]-p2[1]) == 0 and float(p[0]-p2[0])*(p[0]-p1[0]) < 0:
                    return False

            elif float(p1[0]-p2[0])/(p1[1]-p2[1]) == float(p[0]-p2[0])/(p[1]-p2[1]) and float(p[1]-p2[1])*(p[1]-p1[1]) < 0:
                return False
        return True

    # Coordinates of the room boundaries
    bottom_left = [0, 0]
    bottom_right = [dimensions[0], 0]
    top_left = [0, dimensions[1]]
    top_right = [dimensions[0], dimensions[1]]
    global no_directions
    no_directions = 0

    def recurse_image_distance(your_position, your_position_mirror, guard_position_mirror,
                               bottom_left, bottom_right, top_left, top_right,positions_seen):
        global no_directions
        if compute_dist(your_position, guard_position_mirror) <= distance:
            # if your_position_mirror != your_position:
            positions_seen.append(your_position_mirror)
            if is_not_on_way(your_position, guard_position_mirror, positions_seen):
                #print(your_position, guard_position_mirror)
                no_directions += 1

            positions_seen.append(guard_position_mirror)
            fixed_box = list([bottom_left, bottom_right, top_left, top_right])
            # Mirror wrt top
            your_position_mirror1 = [your_position_mirror[0], your_position_mirror[1] + 2*(top_left[1]-your_position_mirror[1])]
            if your_position_mirror1 not in positions_seen:
                guard_position_mirror1= [guard_position_mirror[0], guard_position_mirror[1] + 2*(top_left[1]-guard_position_mirror[1])]
                bottom_left = top_left
                bottom_right = top_right
                top_left = [bottom_left[0], bottom_left[1]+dimensions[1]]
                top_right = [bottom_right[0], bottom_right[1]+dimensions[1]]
                recurse_image_distance(your_position, your_position_mirror1, guard_position_mirror1,
                                       bottom_left, bottom_right, top_left, top_right, positions_seen)

            # Mirror wrt bottom
            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror2 = [
                        your_position_mirror[0], your_position_mirror[1] -
                        2*(your_position_mirror[1] - bottom_left[1])]

            if your_position_mirror2 not in positions_seen:
                guard_position_mirror2 = [
                guard_position_mirror[0], guard_position_mirror[1] - 2*(guard_position_mirror[1] - bottom_left[1])]
                top_left = bottom_left
                top_right = bottom_right
                bottom_left = [top_left[0], top_left[1] - dimensions[1]]
                bottom_right = [top_right[0], top_right[1] - dimensions[1]]
                recurse_image_distance(your_position, your_position_mirror2, guard_position_mirror2,
                                       bottom_left, bottom_right, top_left, top_right, positions_seen)

            # Mirror wrt left

            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror3 = [
                your_position_mirror[0] - 2 * (your_position_mirror[0] - bottom_left[0]), your_position_mirror[1]]
            if your_position_mirror3 not in positions_seen:
                guard_position_mirror3 = [
                    guard_position_mirror[0] - 2 * (guard_position_mirror[0] - bottom_left[0]),
                    guard_position_mirror[1]]
                top_right = top_left
                bottom_right = bottom_left
                top_left = [top_right[0]-dimensions[0], top_right[1]]
                bottom_left = [bottom_right[0]-dimensions[0], bottom_right[1]]
                recurse_image_distance(your_position, your_position_mirror3, guard_position_mirror3,
                                       bottom_left, bottom_right, top_left, top_right, positions_seen)

            # Mirror wrt right
            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror4 = [
                your_position_mirror[0] + 2 * (bottom_right[0] - your_position_mirror[0]), your_position_mirror[1]]
            if your_position_mirror4 not in positions_seen:
                guard_position_mirror4 = [
                    guard_position_mirror[0] + 2 * (bottom_right[0] - guard_position_mirror[0]),
                    guard_position_mirror[1]]
                top_left = top_right
                bottom_left = bottom_right
                top_right = [top_left[0] + dimensions[0], top_left[1]]
                bottom_right = [bottom_left[0] + dimensions[0], bottom_left[1]]
                recurse_image_distance(your_position, your_position_mirror4, guard_position_mirror4,
                                       bottom_left, bottom_right, top_left, top_right, positions_seen)

        else:

            positions_seen.append(your_position_mirror)
            positions_seen.append(guard_position_mirror)

        return

    recurse_image_distance(your_position, your_position, guard_position,
                           bottom_left, bottom_right, top_left, top_right, [])

    return no_directions




def solution(dimensions, your_position, guard_position, distance):
    # Your code here
    def compute_dist(p1,p2):
        return math.hypot(float(p1[0]-p2[0]),float(p1[1]-p2[1]))#((float(p1[0]-p2[0]))**2 + (float(p1[1]-p2[1]))**2)**0.5

    def is_not_on_way(p1,p2, plist):
        for p in plist:
            if p != p1 and p != p2 and (p1[1] - p2[1]) == 0 or (p[1]-p2[1]) == 0:
                if (p1[1] - p2[1]) == 0 and (p[1]-p2[1]) == 0 and float(p[0]-p2[0])*float(p[0]-p1[0]) < 0:
                    return False

            elif p != p1 and p != p2 and float(p1[0]-p2[0])/float(p1[1]-p2[1]) == \
                    float(p[0]-p2[0])/float(p[1]-p2[1]) and float(p[1]-p2[1])*float(p[1]-p1[1]) < 0:
                return False
        return True

    # Coordinates of the room boundaries
    bottom_left = [0, 0]
    bottom_right = [dimensions[0], 0]
    top_left = [0, dimensions[1]]
    top_right = [dimensions[0], dimensions[1]]
    no_directions = 0
    positions_seen = [your_position,guard_position]
    position_to_visit = [(your_position,guard_position, bottom_left, bottom_right, top_left, top_right)]
    tot_guard_positions = []
    while position_to_visit:
        your_position_mirror,guard_position_mirror,bottom_left, bottom_right,\
        top_left, top_right = position_to_visit.pop(0)
        if compute_dist(your_position, guard_position_mirror) <= distance:
            # if your_position_mirror != your_position:
            if is_not_on_way(your_position, guard_position_mirror, positions_seen):
                #print(your_position, your_position_mirror)
                if guard_position_mirror in tot_guard_positions:
                    continue
                tot_guard_positions.append(guard_position_mirror)
                no_directions += 1



            fixed_box = list([bottom_left, bottom_right, top_left, top_right])
            # Mirror wrt top
            your_position_mirror1 = [your_position_mirror[0],
                                     your_position_mirror[1] + 2 * (top_left[1] - your_position_mirror[1])]
            if your_position_mirror1 not in positions_seen:
                guard_position_mirror1 = [guard_position_mirror[0],
                                          guard_position_mirror[1] + 2 * (top_left[1] - guard_position_mirror[1])]
                bottom_left = top_left
                bottom_right = top_right
                top_left = [bottom_left[0], bottom_left[1] + dimensions[1]]
                top_right = [bottom_right[0], bottom_right[1] + dimensions[1]]
                position_to_visit.append((your_position_mirror1, guard_position_mirror1,
                                       bottom_left, bottom_right, top_left, top_right))

            # Mirror wrt bottom
            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror2 = [
                your_position_mirror[0], your_position_mirror[1] -
                                         2 * (your_position_mirror[1] - bottom_left[1])]

            if your_position_mirror2 not in positions_seen:
                guard_position_mirror2 = [
                    guard_position_mirror[0],
                    guard_position_mirror[1] - 2 * (guard_position_mirror[1] - bottom_left[1])]
                top_left = bottom_left
                top_right = bottom_right
                bottom_left = [top_left[0], top_left[1] - dimensions[1]]
                bottom_right = [top_right[0], top_right[1] - dimensions[1]]
                position_to_visit.append((your_position_mirror2, guard_position_mirror2,
                                       bottom_left, bottom_right, top_left, top_right))

            # Mirror wrt left

            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror3 = [
                your_position_mirror[0] - 2 * (your_position_mirror[0] - bottom_left[0]), your_position_mirror[1]]
            if your_position_mirror3 not in positions_seen:
                guard_position_mirror3 = [
                    guard_position_mirror[0] - 2 * (guard_position_mirror[0] - bottom_left[0]),
                    guard_position_mirror[1]]
                top_right = top_left
                bottom_right = bottom_left
                top_left = [top_right[0] - dimensions[0], top_right[1]]
                bottom_left = [bottom_right[0] - dimensions[0], bottom_right[1]]
                position_to_visit.append(( your_position_mirror3, guard_position_mirror3,
                                       bottom_left, bottom_right, top_left, top_right))

            # Mirror wrt right
            bottom_left, bottom_right, top_left, top_right = fixed_box
            your_position_mirror4 = [
                your_position_mirror[0] + 2 * (bottom_right[0] - your_position_mirror[0]), your_position_mirror[1]]
            if your_position_mirror4 not in positions_seen:
                guard_position_mirror4 = [
                    guard_position_mirror[0] + 2 * (bottom_right[0] - guard_position_mirror[0]),
                    guard_position_mirror[1]]
                top_left = top_right
                bottom_left = bottom_right
                top_right = [top_left[0] + dimensions[0], top_left[1]]
                bottom_right = [bottom_left[0] + dimensions[0], bottom_left[1]]
                position_to_visit.append((your_position_mirror4, guard_position_mirror4,
                                       bottom_left, bottom_right, top_left, top_right))

            positions_seen.append(your_position_mirror1)
            positions_seen.append(your_position_mirror2)
            positions_seen.append(your_position_mirror3)
            positions_seen.append(your_position_mirror4)
            positions_seen.append(guard_position_mirror1)
            positions_seen.append(guard_position_mirror2)
            positions_seen.append(guard_position_mirror3)
            positions_seen.append(guard_position_mirror4)




    return no_directions


'''
https://gist.github.com/junaid1460/ab6da07a204e7f21e622dbd91632884e
'''

import math


def generate_dist_vector(size, start, tot_length, length):
    tmp = [start]
    count = 0
    l, r = -length, tot_length - length
    for i in range(size):
        left = tmp[0]
        right = tmp[count]
        left += (l * 2)
        right += (r * 2)
        l, r = -r, -l
        tmp = [left] + tmp + [right]
        count += 2
    return tmp


def make_mat(vec1, vec2):
    mat = []
    count = 0
    for i in vec2:
        mat.append([])
        for j in vec1:
            mat[count].append((j, i))
        count += 1
    return mat


def translate(x, y, vec):
    mat = []
    count = 0
    for i in vec:
        mat.append([])
        for j in i:
            mat[count].append((j[0] + x, j[1] + y))
        # print mat[count]
        count += 1

    return mat


def serialize(vec):
    start = int(len(vec) / 2)
    elms = [vec[start][start]]
    count = 3
    start -= 1
    while (start >= 0):
        x = start
        y = start
        for j in range(1, count):
            x += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y += 1
            elms += [vec[y][x]]
        for j in range(1, count):
            x -= 1
            elms += [vec[y][x]]
        for j in range(1, count):
            y -= 1
            elms += [vec[y][x]]

        start -= 1
        count += 2
    return elms


def key(x, y):
    return format(math.atan2(x, y), '.32f')


def dist(x, y):
    return math.hypot(x, y)


def calc(cap, bad, distance):
    visited = {}
    l = len(cap)
    count = 0
    for i in range(l):
        ce = cap[i]
        be = bad[i]
        # print(ce,be)

        visited[key(ce[0], ce[1])] = True
        if distance - dist(be[0], be[1]) >= 0:
            k = key(be[0], be[1])
            if k not in visited:
                count += 1
                visited[k] = True
        else:
            k = key(be[0], be[1])
            visited[k] = True
            # else:
            #     print (be[0], be[1]), "is there" , k
        # else:
        #     print "distance is more", dist(be[0], be[1])

    # print visited
    return count


def solution1(dimensions, captain, badguy, distance):
    _x = 0
    _y = 1
    tx = captain[_x]
    ty = captain[_y]
    width = dimensions[0]
    height = dimensions[1]
    mat_size = int(math.ceil(max(distance / width, distance / height))) + 1
    bad_x = generate_dist_vector(mat_size, badguy[_x], width, badguy[_x])
    bad_y = generate_dist_vector(mat_size, badguy[_y], height, badguy[_y])
    cap_x = generate_dist_vector(mat_size, captain[_x], width, captain[_x])
    cap_y = generate_dist_vector(mat_size, captain[_y], height, captain[_y])
    # print
    elms_bad = serialize(translate(-tx, -ty, make_mat(bad_x, bad_y)))
    # print
    # print elms_bad
    # print
    # print
    elms_cap = serialize(translate(-tx, -ty, make_mat(cap_x, cap_y)))
    # print
    # print elms_cap

    return calc(elms_cap, elms_bad, distance)
    # print
    # print translate(tx, ty,make_mat(cap_x, cap_y))


print(solution([42, 59], [34, 44], [6, 34], 5000))