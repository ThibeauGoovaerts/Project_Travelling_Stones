import { createRouter, createWebHistory } from "vue-router";
import Personne from "../views/Personne.vue";
import Login from "../views/LoginView.vue";
import Calloux from "../views/CallouxView.vue";
import Decouverte from "../views/DecouverteView.vue";
import http from "../http-login"
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Login,
    },
    {
      path: "/callouxRedirect",
      name: "callouxRedirect",
      component: () => import("../views/CallouxRedirect.vue"),
    },
    {
      path: "/calloux",
      name: "Calloux",
      component: Calloux,
    },
    {
      path: "/decouverte",
      name: "Decouverte",
      component: Decouverte,
    },
    {
      path: "/decouverteRedirect",
      name: "decouverteRedirect",
      component: () => import("../views/DecouverteRedirect.vue"),
    },
    {
      path: "/mapViewCalloux/:nb",
      name: "mapViewCalloux",
      component: () => import("../views/CallouxMapView.vue"),
      props: true,
    },{
      path: "/maintenance",
      name: "maintenance",
      component: () => import("../views/MaintenanceView.vue"),
    },
  ],
});

router.beforeEach(async (to, from, next) => {
  const publicPages = [
    '/',
    '/maintenance',
  ]

  let response = await http.get('maintenance');

  let publicEnvVar = response.data.maintenance

  if (publicEnvVar==="true" && to.path != '/maintenance'){
    next("/maintenance");
  }else if (publicEnvVar==="true" && to.path == '/maintenance'){
    next();
  }else if (to.path === '/maintenance'){
    next('/');
  }else{
      const authRequired = !publicPages.includes(to.path)
      const loggedIn = cookies.get('access')
      if (authRequired && !loggedIn) {
        next('/')
      } else {
        if (authRequired){
          try{
            await http.post("token/verifie", {
              "token": loggedIn
            })
            if (publicEnvVar==="true"){
              next('/')
            }else{
              next()
            }

          }catch (error){
            const response = await http.post("token/refresh", {
              "refresh": cookies.get('refresh')
            })
            if (response.data.access){
              cookies.set('access', response.data.access);
              if (publicEnvVar==="true"){
                next('/')
              }else{
                next()
              }

            }else{
              next('/')
            }
          }
        }else{
          next()
        }
      }
  }
})

export default router;
