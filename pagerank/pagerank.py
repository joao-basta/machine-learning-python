import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    prop_distribution = {}
    n_pages = len(corpus)
    linked_pages = corpus[page]
    if len (linked_pages) == 0:
        for p in corpus:
            prop_distribution[p] = 1/n_pages
        return prop_distribution
    


    random_prob = (1- damping_factor)/ n_pages

    link_prob = damping_factor / len(linked_pages)

    for p in corpus:
        prop_distribution[p] = random_prob
    if p in linked_pages:
        prop_distribution[p] = link_prob
    return prop_distribution


    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    visits = {page:0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))
    visits[current_page] +=1

    for i in range (n-1):
        probabilities = transition_model(corpus, current_page, damping_factor)
        next_page_list = random.choices(list(probabilities.keys()),weights=list(probabilities.values()), k=1)
        
        current_page = next_page_list[0]

        visits[current_page] +=1
    pagerank={}
    for page in visits:
        pagerank[page] = visits[page] / n

    return pagerank

    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    
    ranks = {page: 1 / num_pages for page in corpus}

    while True:
        new_ranks = {}

        for p in corpus:
            random_jump_prob = (1-damping_factor)/num_pages
            
            sum_links = 0            

            for i in corpus:

                if p in corpus[i]:
                    sum_links += ranks[i]/ len(corpus[i])
            
                elif len(corpus[i]) == 0:
                    sum_links += ranks[i]/num_pages

            new_ranks[p] = random_jump_prob + (damping_factor* sum_links)
            
        converged = True
        
        for p in corpus:
            if abs (new_ranks[p] - ranks[p]) > 0.001:
                converged = False
                break

        ranks = new_ranks
        
        if converged:
            return ranks
        
    raise NotImplementedError


if __name__ == "__main__":
    main()
