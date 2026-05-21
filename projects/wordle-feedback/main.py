def compute_feedback(target, guess):
    target = target.upper()
    guess = guess.upper()
    result = ["."] * len(guess)
    used = [False] * len(target)

    for i in range(min(len(target), len(guess))):
        if guess[i] == target[i]:
            result[i] = guess[i]
            used[i] = True

    for i in range(len(guess)):
        if result[i] != ".":
            continue

        for j in range(len(target)):
            if not used[j] and guess[i] == target[j]:
                result[i] = guess[i].lower()
                used[j] = True
                break

    return "".join(result)


def main():
    target = input().strip()
    guess = input().strip()
    print(compute_feedback(target, guess))


if __name__ == "__main__":
    main()
