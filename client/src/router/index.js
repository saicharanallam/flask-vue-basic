import Vue from 'vue';
import VueRouter from 'vue-router';
// import Home from '../views/Home.vue';
import Ping from '../components/Ping.vue';
import Books from '../components/Books.vue';
import Pdf1 from '../components/Pdf1.vue';
import Pdf2 from '../components/Pdf2.vue';

Vue.use(VueRouter);

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home,
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  // },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/',
    name: 'Books',
    component: Books,
  },
  {
    path: '/pdf1',
    name: 'pdf1',
    component: Pdf1,
  },
  {
    path: '/pdf2',
    name: 'pdf2',
    component: Pdf2,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
