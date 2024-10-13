def recover_secret(triplets):
    output = {c : i for i, c in enumerate(set([item for sublist in triplets for item in sublist]))}
    swaped = True
    while swaped:
        swaped = False
        for triplet in triplets:
            if output[triplet[0]] > output[triplet[1]]:
                output[triplet[0]], output[triplet[1]] = output[triplet[1]], output[triplet[0]]
                swaped = True
            if output[triplet[1]] > output[triplet[2]]:
                output[triplet[1]], output[triplet[2]] = output[triplet[2]], output[triplet[1]]
                swaped = True
    temp = sorted([(i, c) for c, i in output.items()], key=lambda x: x[0])
    return ''.join([c for _, c in temp])
