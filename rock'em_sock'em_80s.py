def fight(robot_1,robot_2, tactics):
    m1,m2 = {},{}
    m1,m2 = (robot_2,robot_1) if robot_2['speed'] > robot_1['speed'] else (robot_1,robot_2)
    m1['tactics'],m2['tactics'] = sorted(m1['tactics'], reverse = True), sorted(m2['tactics'], reverse = True)
    w = '' #if there is a winner
    m1_go,m2_go = False,False #if they can go, i.e if tactics left
    while m1['tactics'] or m2['tactics']: #someone has tactics left
        if m1['tactics']: #checks if they can go
            m1_go = True
        else:
            m1_go = False
        if m2['tactics']: #checks if they can go
            m2_go = True
        else:
            m2_go = False

        if m1_go:
            m2['health'] -= tactics[m1['tactics'][-1]]
            m1['tactics'].pop()
            if m2['health'] <= 0:
                w = m1['name']
                break

        if m2_go:
            m1['health'] -= tactics[m2['tactics'][-1]]
            m2['tactics'].pop()
            if m1['health'] <= 0:
                w = m2['name']
                break

    if w: #if there is a winner otherwise w = '' so False
        return '{} has won the fight.'.format(w)
    else: #have to check tie or winner
        if m1['health'] > m2['health']:
            return '{} has won the fight.'.format(m1['name'])
        elif m2['health'] > m1['health']:
            return '{} has won the fight.'.format(m2['name'])
        else:
            return 'The fight was a draw.'

robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
print(fight(robot_1, robot_2, tactics))
