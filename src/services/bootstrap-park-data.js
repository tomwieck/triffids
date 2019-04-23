import { parkService } from "./Park.service";

import { SET_ALL_PARKS } from "../store/mutation-types";

let resolveApiRequest;

export const apiRequestPromise = new Promise((resolve) => {
	resolveApiRequest = resolve;
});

export default async function bootstrapDataPlugin(store) {
	await parkService.parks()
		.then((allParksData) => {
			store.commit(SET_ALL_PARKS, allParksData);
			resolveApiRequest && resolveApiRequest();
		});
}
