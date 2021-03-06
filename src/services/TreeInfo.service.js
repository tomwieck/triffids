import Vue from 'vue'
import wiki from 'wikijs'

export const treeInfoService = {
    getTreeInfo,
    getImageLink,
    getPageLink
}

const treedata = require('../assets/trees/treenames.json')

/**
 * lookup this tree in the json file and get other details
 * 
 * see end of file to view the fields
 * 
 * @param {string} latin_code the latin code to lookup in the json
 */
async function getTreeInfo(latin_code) {
    const tree = treedata.filter((t) => {
        return t.latin_code == latin_code
    })[0];
    if (!tree) {
        return {
            latin_code: latin_code,
            latin_name: 'Not found',
            common_name: "Not found",
            full_common_name: 'Details not found',
            wiki_data: 'No Wikipedia data available',
            wiki_image: ''
        };
    }
    const term = tree.wiki_page.split('/').pop();
    const wiki_options = {
        apiUrl: "https://en.wikipedia.org/w/api.php"
    }
    try {
        Vue.$log.info('TreeInfo.service: calling out to wiki with ', term)
        const content = await wiki(wiki_options).page(term).then(page => page.summary())
        tree.wiki_data = content
    } catch (error) {
        Vue.$log.error('getTreeInfo:error ', error)
        tree.wiki_data = 'Error collecting data from Wikipedia'
    }
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

/*
 *     {
        "latin_code": "ACC2",
        "latin_name": "Acer campestre",
        "common_name": "Field Maple",
        "full_common_name": "Field maple",
        "wiki_page": "https://en.wikipedia.org/wiki/Acer_campestre",
        "wiki_image": "https://upload.wikimedia.org/wikipedia/commons/a/af/Acer_campestre_in_Appennino2.jpg"
    },
 */