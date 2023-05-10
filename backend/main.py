import purchase
import generate

if __name__ == '__main__':
    acc = purchase.Account()
    gpt = generate.GPT()


    acc.placeBuyOrder(gpt.Recommend())