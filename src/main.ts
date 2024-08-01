import "@/assets/theme.css";

import { createApp } from "vue";
import { createMemoryHistory, createRouter } from "vue-router";

import App from "./App.vue";
import RootView from "./views/RootView.vue";
import InfiniteView from "./views/InfiniteView.vue";

const routes = [
  { path: "/", component: RootView },
  { path: "/infinite", component: InfiniteView },
];

const router = createRouter({ history: createMemoryHistory(), routes });

createApp(App).use(router).mount("#app");
