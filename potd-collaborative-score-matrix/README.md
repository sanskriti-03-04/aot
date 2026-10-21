# THE COLLABORATIVE SCORE MATRIX

Beginner | linear-algebra

**Difficulty:** Easy
**Tags:** Linear Algebra

---

### Story

Spotify's collaborative-filtering recommendation score, at its absolute simplest, is one matrix
multiply between user and item embedding matrices. Every fancier recommender in this track builds on
getting this multiply right.

---

### The Math

```
R_hat = U V^T
```

### Input Format

```
n_users n_items d
U (n_users x d, row-major)
V (n_items x d, row-major)
```

### Output Format

`R_hat`, `n_users x n_items` matrix, 6 decimals.

### Constraints

- `1 <= n_users, n_items <= 500`, `1 <= d <= 128`
- Time limit: 1.0 second.

---

### Example

**Input**

```
2 3 2
1 0
0 1
2 1
1 2
0 1
```

**Output**

```
2.000000 1.000000 0.000000
1.000000 2.000000 1.000000
```
