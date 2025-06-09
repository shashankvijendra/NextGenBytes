package main

import (
	"net/http"
	"strconv"
	"sync"

	"github.com/gin-gonic/gin"
)

// Item represents a simple data structure
type Item struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Price int    `json:"price"`
}

var (
	items   = make(map[int]Item) // in-memory store
	nextID  = 1
	itemsMu sync.Mutex // mutex for concurrent access
)

func main() {
	r := gin.Default()

	// Create
	r.POST("/items", func(c *gin.Context) {
		var newItem Item
		if err := c.ShouldBindJSON(&newItem); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		itemsMu.Lock()
		newItem.ID = nextID
		nextID++
		items[newItem.ID] = newItem
		itemsMu.Unlock()

		c.JSON(http.StatusCreated, newItem)
	})

	// Read all
	r.GET("/items", func(c *gin.Context) {
		itemsMu.Lock()
		defer itemsMu.Unlock()

		var list []Item
		for _, item := range items {
			list = append(list, item)
		}
		c.JSON(http.StatusOK, list)
	})

	// Read one
	r.GET("/items/:id", func(c *gin.Context) {
		id, err := strconv.Atoi(c.Param("id"))
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
			return
		}

		itemsMu.Lock()
		item, exists := items[id]
		itemsMu.Unlock()

		if !exists {
			c.JSON(http.StatusNotFound, gin.H{"error": "Item not found"})
			return
		}

		c.JSON(http.StatusOK, item)
	})

	// Update
	r.PUT("/items/:id", func(c *gin.Context) {
		id, err := strconv.Atoi(c.Param("id"))
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
			return
		}

		var updatedItem Item
		if err := c.ShouldBindJSON(&updatedItem); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		updatedItem.ID = id

		itemsMu.Lock()
		_, exists := items[id]
		if !exists {
			itemsMu.Unlock()
			c.JSON(http.StatusNotFound, gin.H{"error": "Item not found"})
			return
		}
		items[id] = updatedItem
		itemsMu.Unlock()

		c.JSON(http.StatusOK, updatedItem)
	})

	// Delete
	r.DELETE("/items/:id", func(c *gin.Context) {
		id, err := strconv.Atoi(c.Param("id"))
		if err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
			return
		}

		itemsMu.Lock()
		_, exists := items[id]
		if !exists {
			itemsMu.Unlock()
			c.JSON(http.StatusNotFound, gin.H{"error": "Item not found"})
			return
		}
		delete(items, id)
		itemsMu.Unlock()

		c.Status(http.StatusNoContent)
	})

	r.Run(":8080")
}
