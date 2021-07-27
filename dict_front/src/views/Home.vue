<template>
  <div>
        
    <v-btn large color="error">hell</v-btn>
    <v-data-table> </v-data-table>
    <div v-for="word in words" :key="word.id">
      {{ word.original_word }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      words: [],
    };
  },

  components: {
  },
  mounted() {
    this.getWords();
  },
  methods: {
    getWords() {
      axios
        .get("/api/v1/words/")
        .then((resp) => {
          this.words = resp.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
