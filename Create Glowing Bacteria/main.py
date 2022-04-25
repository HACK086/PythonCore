COMPLEMENTARY = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def complementary_strand(strand):
    return ''.join(COMPLEMENTARY.get(c, c) for c in strand)


def stage():
    with open(input(), 'r') as file:
        origin_stand = file.readline().strip()
        restriction = file.readline().strip()
        gen = file.readline().strip()
        prefix, suffix = file.readline().strip().split(maxsplit=2)

    index = origin_stand.find(restriction) + 1

    top = gen.find(prefix) + 1
    end = gen.rfind(suffix) + 1

    modified = "".join((
        origin_stand[:index],
        gen[top:end],
        origin_stand[index:]
    ))
    print(modified, complementary_strand(modified), sep='\n')


if __name__ == "__main__":
    stage()