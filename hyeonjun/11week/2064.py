import sys
input = sys.stdin.readline


if __name__ == "__main__":
    def find_start(start_idx, bin_idx):
        for i in range(4):
            for j in range(len(bin(network_address[i]))-2):
                if bin(network_address[i])[j+2] == '1':
                    start_idx, bin_idx = i, len(bin(network_address[i]))-j-2
                    return start_idx, 8-bin_idx
        return 4, 0

    n = int(input())
    IPs = [list(map(int, input().rstrip().split('.'))) for _ in range(n)]

    network_address = [0 for _ in range(4)]
    network_mask = ['' for _ in range(4)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(4):
                network_address[k] |= IPs[i][k] ^ IPs[j][k]

    start_idx, bin_idx = find_start(0, 0)

    for i in range(4):
        for j in range(8):
            if (i == start_idx and j >= bin_idx) or i > start_idx:
                network_mask[i] += '0'
            else:
                network_mask[i] += '1'

    for i in range(4):
        network_mask[i] = int(network_mask[i], 2)
        network_address[i] = IPs[0][i] & network_mask[i]

    print('.'.join(map(str, network_address)))
    print('.'.join(map(str, network_mask)))
