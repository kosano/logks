<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" v-for="(item, i) in resouces" :key="i">
      <q-card-section class="bg-green text-white">
        <div class="text-h6">{{ item }}</div>
        <div class="text-blue">deployment</div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn flat>Action 1</q-btn>
        <q-btn flat>Action 2</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      resouces: [],
    };
  },
  methods: {
    getDeployments(namespace) {
      this.resouces = [];
      this.$api
        .get("/api/v1/namespace/all/deployments")
        .then((res) => {
          res.data.data.forEach((item) => {
            this.resouces.push(item);
          });
        })
        .catch((err) => {
          this.$q.notify({
            type: "negative",
            message: `Get Deployments failed. ${err}`,
          });
        });
    },
  },
  mounted() {
    this.getDeployments("all");
  },
};
</script>