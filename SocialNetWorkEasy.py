n, k = list(map(int, input().split()))
 
running_list = []
membership_set = set()

input_list = list(input().split())
for text in input_list:
    if text in membership_set:
        continue

    if (len(running_list) < k):
        running_list.append(text)
        membership_set.add(text)
    else:
        membership_set.discard(running_list[0])
        del running_list[0]
        
        running_list.append(text)
        membership_set.add(text)
        
        continue

print(len(running_list))
print(' '.join(running_list[::-1]))