import {
	SET_ALL_PARKS
} from './mutation-types';

const mutations = {
 [SET_ALL_PARKS]: (state, payload) => {
   state.allParkNames = payload;
 }

}

export default mutations;
