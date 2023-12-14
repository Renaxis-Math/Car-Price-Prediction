def pow2(N):
    ans = 0
    for i in range(64):
        x = 1
        if (N & (x << i)) > 0:
            ans += 1
    return ans

def minimumChunksRequired(m, chunk_list):
    chunk_list.sort(key=lambda x: x[0])
    
    last_chunk_num = 1
    ans = 0
    
    # Calculating length of un-uploaded items
    for i in range(len(chunk_list)):
        start = chunk_list[i][0]
        end = chunk_list[i][1]
        ans += pow2(start - last_chunk_num)
        last_chunk_num = end + 1

    if chunk_list[-1][1] != total:
        ans += pow2(total - chunk_list[-1][1])
        
    return ans