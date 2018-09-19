from rnn_model import RNNModel
import torch

def swipe_convert(src):
    src = [i - 64 for i in src]
    length = len(src)
    if len(src) > 10:
        src = src[:10]
        length = 10
    else:
        src = src + [0] * (10 - len(src))

    src = torch.LongTensor([src])
    length = torch.LongTensor([length])
    model = RNNModel('LSTM', 27, 1, 10, 1, 0.2)
    # Load the best saved model.
    with open('model.pt', 'rb') as f:
        model = torch.load(f)
        # after load the rnn params are not a continuous chunk of memory
        # this makes them a continuous chunk, and will speed up forward pass
        model.rnn.flatten_parameters()
    model.eval()
    hidden = model.init_hidden(1)

    with torch.no_grad():
        output, hidden = model(src, length, hidden)
        pred = output.max(1, keepdim=True)[1]
        return pred.item()


if __name__ == '__main__':
    print(swipe_convert([70, 74, 68, 75, 76, 83]))
