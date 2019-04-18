import { parkService } from "./Park.service";

import { SET_ALL_PARKS } from "../store/mutation-types";

let resolveApiRequest;

export const apiRequestPromise = new Promise((resolve) => {
	resolveApiRequest = resolve;
});

export default async function bootstrapDataPlugin(store) {
	console.log(parkService);
	await parkService.parks()
		.then((allParksData) => {
			console.log(allParksData);
			store.commit(SET_ALL_PARKS, allParksData);
			resolveApiRequest && resolveApiRequest();
		});
}
