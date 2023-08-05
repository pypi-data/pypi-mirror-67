import os
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import torch
from torch import optim
from torch.nn import functional as F

from data import get_data
from n_beats.model import NBeatsNet

CHECKPOINT_NAME = 'nbeats-fiting-checkpoint.th'


###############################################################################################################
###############################################################################################################
# from util import set_root_dir
####################################################################################################
class Model:
    def __init__(self,
        learning_rate=0.001,
        num_layers=2,
        size=None,
        size_layer=128,
        output_size=None,
        forget_bias=0.1,
        timestep=5,
        epoch=5,
    ):
        self.epoch = epoch
        self.stats = {"loss":0.0,
                      "loss_history": [] }
        self.timestep = timestep









def fit(model, data_pars):
    df = get_dataset(data_pars)

    #########
    nlog_freq=100
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    for i in range(model.epoch):
        total_loss = 0


        ######## Model specific  ########################################






        ####### End Model specific    ##################################


        total_loss /= df.shape[0] // model.timestep
        model.stats["loss"] = total_loss

        if (i + 1) % nlog_freq == 0:
            print("epoch:", i + 1, "avg loss:", total_loss)
    return sess



def stats_compute(model, sess, df, ):
    # Compute stats on training
    arr_out = predict(model, sess, df, )
    return model.stats



def predict(model, sess, data_pars, ):

    df = get_dataset(data_pars)


    return output_predict



def reset_model():
    tf.reset_default_graph()








def fit(model, data_pars):
    args = get_script_arguments()
    device = torch.device('cuda') if not args.disable_cuda and torch.cuda.is_available() else torch.device('cpu')
    forecast_length = 10
    backcast_length = 5 * forecast_length
    batch_size = 100  # greater than 4 for viz

    data_gen = get_data(batch_size, backcast_length, forecast_length,
                        signal_type='seasonality', random=True)

    print('--- Model ---')
    net = NBeatsNet(device=device,
                    stack_types=[NBeatsNet.TREND_BLOCK, NBeatsNet.SEASONALITY_BLOCK],
                    forecast_length=forecast_length,
                    thetas_dims=[2, 8],
                    nb_blocks_per_stack=3,
                    backcast_length=backcast_length,
                    hidden_layer_units=1024,
                    share_weights_in_stack=False)

    # net = NBeatsNet(device=device,
    #                 stack_types=[NBeatsNet.GENERIC_BLOCK, NBeatsNet.GENERIC_BLOCK],
    #                 forecast_length=forecast_length,
    #                 thetas_dims=[7, 8],
    #                 nb_blocks_per_stack=3,
    #                 backcast_length=backcast_length,
    #                 hidden_layer_units=128,
    #                 share_weights_in_stack=False)

    optimiser = optim.Adam(net.parameters())

    def plot_model(x, target, grad_step):
        if not args.disable_plot:
            print('plot()')
            plot(net, x, target, backcast_length, forecast_length, grad_step)

    simple_fit(net, optimiser, data_gen, plot_model, device)


def simple_fit(net, optimiser, data_generator, on_save_callback, device, max_grad_steps=10000):
    print('--- fiting ---')
    initial_grad_step = load(net, optimiser)
    for grad_step, (x, target) in enumerate(data_generator):
        grad_step += initial_grad_step
        optimiser.zero_grad()
        net.fit()
        backcast, forecast = net(torch.tensor(x, dtype=torch.float).to(device))
        loss = F.mse_loss(forecast, torch.tensor(target, dtype=torch.float).to(device))
        loss.backward()
        optimiser.step()
        print(f'grad_step = {str(grad_step).zfill(6)}, loss = {loss.item():.6f}')
        if grad_step % 1000 == 0 or (grad_step < 1000 and grad_step % 100 == 0):
            with torch.no_grad():
                save(net, optimiser, grad_step)
                if on_save_callback is not None:
                    on_save_callback(x, target, grad_step)
        if grad_step > max_grad_steps:
            print('Finished.')
            break


def save(model, optimiser, grad_step):
    torch.save({
        'grad_step': grad_step,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimiser.state_dict(),
    }, CHECKPOINT_NAME)


def load(model, optimiser):
    if os.path.exists(CHECKPOINT_NAME):
        checkpoint = torch.load(CHECKPOINT_NAME)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimiser.load_state_dict(checkpoint['optimizer_state_dict'])
        grad_step = checkpoint['grad_step']
        print(f'Restored checkpoint from {CHECKPOINT_NAME}.')
        return grad_step
    return 0








######################################################################################
def plot(net, x, target, backcast_length, forecast_length, grad_step):
    net.eval()
    _, f = net(torch.tensor(x, dtype=torch.float))
    subplots = [221, 222, 223, 224]

    plt.figure(1)
    plt.subplots_adjust(top=0.88)
    for i in range(4):
        ff, xx, yy = f.cpu().numpy()[i], x[i], target[i]
        plt.subplot(subplots[i])
        plt.plot(range(0, backcast_length), xx, color='b')
        plt.plot(range(backcast_length, backcast_length + forecast_length), yy, color='g')
        plt.plot(range(backcast_length, backcast_length + forecast_length), ff, color='r')
        # plt.title(f'step #{grad_step} ({i})')

    output = 'n_beats_{}.png'.format(grad_step)
    plt.savefig(output)
    plt.clf()
    print('Saved image to {}.'.format(output))






def get_script_arguments():
    parser = ArgumentParser(description='N-Beats')
    parser.add_argument('--disable-cuda', action='store_true', help='Disable CUDA')
    parser.add_argument('--disable-plot', action='store_true', help='Disable interactive plots')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    fit()
