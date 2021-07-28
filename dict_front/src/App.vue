<template>
  <v-app>
    <v-main>
      <header>
        <div class="ma-2" style="flex">
          <div style="display: flex; 
          justify-content: flex-end"
          >
          <!-- <v-btn to="/">Home</v-btn> -->
          <!-- <v-btn class="ml-2" color="success">LogIn</v-btn> -->
          <!-- <v-btn class="ml-2" color="success">LogOut</v-btn> -->
          </div>
          <div style="display: flex; 
          justify-content: center">Your Dictionary</div>
        </div>

      </header>

      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
};
</script>
