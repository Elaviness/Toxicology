function scrollToHash(hash) {
    location.hash = "#" + hash;
}

function TSTNode(el, end) {
    this.count = 0;
    this.card = null;
    this.element = el;
    this.isEnd = end;
    this.equal = null;
    this.left = null;
    this.right = null;
    return this;
}

window.toUp = () => {
};

function insertCard(root, smiles, card) {
    if (root.root === null)
        root.root = new TSTNode(smiles[0], false);
    let current = root.root;
    let i = 0;
    for (; i < smiles.length;) {
        let end = undefined;
        const comp = current.element === smiles[i] ? 0 : (current.element > smiles[i] ? 1 : 2);
        switch (comp) {
            case 0: {
                end = i === (smiles.length - 1);
                if (end) {
                    current.isEnd = true;
                    current.card = card;
                } else {
                    if (current.equal === null) {
                        current.equal = new TSTNode(smiles[i + 1], false);
                    }
                    current = current.equal;
                }
                i++;
            }
                break;
            case 1: {
                if (current.left === null) {
                    current.left = new TSTNode(smiles[i], false);
                }
                current = current.left;
            }
                break;
            case 2: {
                if (current.right === null) {
                    current.right = new TSTNode(smiles[i], false);
                }
                current = current.right;
            }
                break;
        }

    }
}

function searchCard(root, smiles) {
    let i = 0;
    let current = root.root;
    for (; i < smiles.length;) {
        const comp = current.element === smiles[i] ? 0 : (current.element > smiles[i] ? 1 : 2);
        switch (comp) {
            case 0: {
                if (current.isEnd && i === smiles.length - 1)
                    return current.card;
                current = current.equal;
                i++;
            }
                break;
            case 1: {
                current = current.left;
            }
                break;
            case 2: {
                current = current.right;
            }
                break;
        }
        if (current === null)
            return null;
    }
}

window.addEventListener("load", () => {
    const cards = document.getElementsByName("card");
    const searchTree = {root: null};
    let lastSelected = null;
    for (let card of cards) {
        const cardSmiles = card.dataset.smiles;
        insertCard(searchTree, cardSmiles, card);
        card.dataset.smiles = "";
        card.dataset.selected = "0";
    }
    const form = document.getElementById("search-form");
    const input = document.getElementById("search-input");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        input.dataset.error = "0";
        scrollToHash("");
        const value = input.value;
        const card = searchCard(searchTree, value);
        if (lastSelected) {
            lastSelected.dataset.selected = "0";
        }
        lastSelected = card;
        if (card) {
            card.dataset.selected = "1";
            scrollToHash(card.id);
        } else {
            input.dataset.error = "1";
        }
    });
    window.toUp = () => {
        if (lastSelected) {
            lastSelected.dataset.selected = "0";
        }
        lastSelected = null;
        scrollToHash("");
        window.scroll({top: 0});
    }
    if (window.location.hash) {
        lastSelected = document.getElementById(window.location.hash.substr(1));
        if (lastSelected) {
            lastSelected.dataset.selected = "1";
        } else {
            scrollToHash("");
        }
    }
    const back = document.getElementsByClassName("back")[0];
    if (window.scrollY > 1024) {
        back.className = "back"
    }
    window.addEventListener("scroll", (e) => {
        if (window.scrollY > 1024) {
            back.className = "back"
        } else {
            back.className = "back hidden-back"
        }
    });
});