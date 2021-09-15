def file():
    l2, l3, c2, c3 = [], [], 0, 0
    with open('users.txt') as users:
        for u in users:
            l = u.strip().split(';')
            try:
                int(l[1])
            except ValueError:
                l3.append({})
                l3[c3]['usarname'], l3[c3]['id'], l3[c3]['first_name'], l3[c3]['last_name'] = l[0], l[1], l[2], l[3]
                c3 += 1
            else:
                l2.append({})
                l2[c2]['usarname'], l2[c2]['id'], l2[c2]['first_name'], l2[c2]['last_name'] = l[0], int(l[1]), l[2], l[3]
                c2 += 1
    with open('wrong_rows.txt', 'w') as wr:
        for i in l3:
            wr.write(str(i) + '\n')
    return l2


print(file())
