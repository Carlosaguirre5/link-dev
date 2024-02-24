<template>
    <div>
        <h1>API Data</h1>
        <ul>
            <li v-for="item in items" :key="item._id.$oid">
                <div>{{ item.marca }}</div>
                <div>{{ item.modelo }}</div>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: []
        };
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await fetch('http://localhost:3000/dev/inventario');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                this.items = data; // Assuming the response is an array of items
            } catch (error) {
                console.error('There was a problem fetching the data:', error);
            }
        }
    }
};
</script>
