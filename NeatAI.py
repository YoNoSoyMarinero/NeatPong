import neat
import os
import pickle

from Game import Game

def test_best_net(config):
    with open("best3.pickle", "rb") as f:
        winner = pickle.load(f)
        winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
        game = Game()
        game.neat_v_human_test_ai(winner_net)

def eval_genomes_v_neat(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = Game()

            force_quit = game.neat_v_neat_train_ai(genome1, genome2, config)
            if force_quit:
                quit()

def eval_genomes_v_bot(genomes, config):
    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        game = Game()
        force_quit = game.neat_v_bot_train_ai(genome, config)
        if force_quit:
            quit()

def run_neat(config):
    #p = neat.Population(config)
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-54')
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes_v_bot, 3)
    with open("best.pickle-4", "wb") as f:
        pickle.dump(winner, f)

def run_neat_against_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-56')
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes_v_neat, 20)
    with open("best4.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_path)
    
test_best_net(config)