import Vue from 'vue'
import wiki from 'wikijs'

export const treeInfoService = {
    getTreeInfo,
    getImageLink,
    getPageLink
}

const treedata = require('../assets/trees/treenames.json')

async function getTreeInfo(latin_code) {
    let tree = treedata.filter((t) => {
        return t.latin_code == latin_code
    })[0];
    const term = tree.wiki_page.split('/').pop();
    try {
        const content = await wiki().page(term).then(page => page.content())
        tree.wiki_data = content[0]['content']
    } catch (error) {
        Vue.$log.error('getTreeInfo:error ', error)
        tree.wiki_data = 'Error collecting data from Wikipedia'
    }
    // temporarily...
    tree.height = '29m';
    tree.girth = '99cm';
    tree.age = '~99';
    return tree
}

function getPageLink(latin_code) {
    let tree = treedata.filter((t) => {
        return t.latin_code == latin_code
    })[0];
    return tree.wiki_page;
}

function getImageLink(latin_code) {
    let tree = treedata.filter((t) => {
        return t.latin_code == latin_code
    })[0];
    return tree.wiki_image;
}