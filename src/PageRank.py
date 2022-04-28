from src.utils.utils import init_graph
from scipy.stats import rankdata    

def PageRank_one_iter(graph, d):
    i=0
    node_list = graph.nodes
    for node in node_list:
        node.update_pagerank(d, len(graph.nodes))
        i=i+1
    
    graph.normalize_pagerank()
    # print(graph.get_pagerank_list())
    # print()


def PageRank(graph, d, iteration=100):
    fb=[0]*len(graph.nodes)
    for i in range(iteration):
        PageRank_one_iter(graph, d)
        pr = graph.get_pagerank_list()
        pos = graph.userfeedback()
        fb[pos]+=1
        updateRanking(graph,pr.copy(),fb.copy())

def updateRanking(graph,pr,fb):

    alpha=0.5
    beta=0.5
    #fb2=fb.copy()
    #pr2=pr.copy()
    norm_fb = [float(i)/sum(fb) for i in fb]
    norm_fb = [x*alpha for x in norm_fb]
    pr = [x*beta for x in pr]
    print(pr)
    print(fb)
    #print([sum(x) for x in zip(norm_fb,pr)])
    ranked = rankdata([sum(x) for x in zip(norm_fb,pr)],method='ordinal')
    #print(ranked)
    #graph.update_ranked_list([sum(x) for x in zip(norm_fb,pr)])
    graph.update_track(ranked)





if __name__ == '__main__':

    iteration = 100
    damping_factor = 0.15

    graph = init_graph('./dataset/graph_4.txt')

    PageRank(iteration, graph, damping_factor)
    print(graph.get_pagerank_list())
