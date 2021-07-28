<template>
  <div>
    <AddWordModal />

    <div style="display: flex; justify-content: center">
      <v-card>
        <v-card-title>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-card-title>

        <v-data-table
          @click:row="selectWord"
          style="width: 600px"
          :headers="headers"
          :items="words"
          :item-class="backgroundRow"
          item-key="id"
          :search="search"
        >
          <template v-slot:[`item.original_word`]="{ item }">
            <div v-if="selectedWord.id === item.id && editMode">
              <v-text-field
                dense
                hide-details
                v-model="selectedWord.original_word"
              ></v-text-field>
            </div>
            <span v-else>{{ item.original_word }}</span>
          </template>

          <template v-slot:[`item.translate_original_word`]="{ item }">
            <div v-if="selectedWord.id === item.id && editMode">
              <v-text-field
                dense
                hide-details
                v-model="selectedWord.translate_original_word"
              ></v-text-field>
            </div>
            <span v-else>{{ item.translate_original_word }}</span>
          </template>
        </v-data-table>
      </v-card>

      <div class="ma-2" style="display: block">
        <div>
          <v-btn width="90" color="success" @click="addWord"> Add </v-btn>
        </div>
        <div class="mt-2">
          <v-btn width="90" color="info" @click="editWord">Edit</v-btn>
        </div>
        <div class="mt-2"><v-btn width="90" color="error">Delete</v-btn></div>
        <div class="mt-2"><v-btn width="90" color="success">Save</v-btn></div>
        <div class="mt-2"><v-btn width="90" color="error">Cancel</v-btn></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main";
import AddWordModal from "../components/AddWordModal.vue";

export default {
  components: {
    AddWordModal,
  },
  name: "Home",
  data() {
    return {
      search: "",
      editMode: false,
      selectedWord: {},
      words: [],
      headers: [
        { text: "Original word", value: "original_word", width: "300" },
        { text: "Translate", value: "translate_original_word", width: "300" },
      ],
    };
  },

  mounted() {
    this.getWords();
  },

  methods: {
    editWord() {
      this.editMode = true;
    },

    backgroundRow(item) {
      return item.id === this.selectedWord.id ? "blue lighten-4" : "";
    },

    selectWord(item) {
      this.selectedWord = item;
    },

    getUpdatedWords(data) {
      console.log(data);
    },

    addWord() {
      eventBus.$emit("showModalAddWord");
    },

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
  created() {
    eventBus.$on("updatedWords", this.getWords);
  },
};
</script>
