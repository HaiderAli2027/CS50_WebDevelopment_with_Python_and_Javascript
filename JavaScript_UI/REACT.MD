# React Core Concepts Reference

---

## How React Works in the Browser

When you load a React app, the browser receives plain HTML, CSS, and JS. React ships as a JavaScript library that runs entirely in the browser (client-side).

**The flow:**

```
index.html  →  loads bundle.js  →  React boots  →  builds Virtual DOM  →  injects into real DOM
```

Your `index.html` usually has just one element:

```html
<div id="root"></div>
```

React targets this div and controls everything inside it.

```javascript
// main.jsx
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

React takes over `#root` and renders your entire UI from that single entry point.

---

## Virtual DOM — The Core Trick

React does NOT update the real DOM directly. It keeps a lightweight copy of the DOM in memory called the **Virtual DOM (VDOM)**.

**How it works under the hood:**

1. You change state → React re-renders the component (produces a new VDOM tree)
2. React **diffs** the new VDOM against the old one (the reconciliation algorithm)
3. React calculates the minimum set of real DOM operations needed
4. React applies only those changes to the real DOM (called **committing**)

```
State change
    ↓
New Virtual DOM tree created
    ↓
Diff old VDOM vs new VDOM  ←— React Fiber does this
    ↓
Patch only changed nodes in real DOM
```

**Why it's fast:** Real DOM manipulation is expensive. React batches & minimizes it.

---

## JSX — HTML Inside JavaScript

JSX is syntactic sugar — it's not real HTML. Babel compiles it to `React.createElement()` calls.

```jsx
// What you write
const el = <h1 className="title">Hello</h1>;

// What Babel compiles it to
const el = React.createElement("h1", { className: "title" }, "Hello");
```

Rules:

- Use `className` instead of `class`
- Self-close empty tags: `<img />`
- Return a single root element (or use `<>...</>` Fragment)
- JavaScript expressions go inside `{}`

```jsx
const name = "Haider";
const el = <p>Hello, {name}!</p>;
```

---

## Components

Components are the building blocks of React UI. They are JavaScript functions (or classes) that return JSX.

```jsx
// Functional Component
function Greeting({ name }) {
  return <h2>Hello, {name}!</h2>;
}

// Usage
<Greeting name="Haider" />;
```

**Rules:**

- Component names must start with a capital letter
- Must return JSX (or null)
- Should be pure — same props → same output

---

## Props

Props (properties) are how parent components pass data to child components. They are **read-only**.

```jsx
function Card({ title, description }) {
  return (
    <div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

// Parent passes props
<Card title="React" description="A UI library" />;
```

Props can be any JS value: strings, numbers, arrays, objects, even functions.

---

## State — `useState`

State is data that lives inside a component and can change over time. When state changes, React re-renders the component.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0); // initial value = 0

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
    </div>
  );
}
```

**Under the hood:**

- `useState` stores state in a linked list tied to the component's fiber node
- Calling `setCount` schedules a re-render
- React re-runs the function and the new `count` value is used

**Never mutate state directly:**

```jsx
// WRONG
count = count + 1;

// RIGHT
setCount(count + 1);
```

---

## Effects — `useEffect`

`useEffect` lets you run side effects (API calls, subscriptions, timers) after render.

```jsx
import { useState, useEffect } from "react";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then((res) => res.json())
      .then((data) => setUser(data));
  }, [userId]); // runs when userId changes

  return <div>{user ? user.name : "Loading..."}</div>;
}
```

**Dependency array behavior:**

| Syntax                  | When it runs         |
| ----------------------- | -------------------- |
| `useEffect(fn)`         | After every render   |
| `useEffect(fn, [])`     | Once — on mount only |
| `useEffect(fn, [x, y])` | When x or y changes  |

**Cleanup function:**

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log("tick"), 1000);
  return () => clearInterval(timer); // cleanup on unmount
}, []);
```

---

## Component Lifecycle (via Hooks)

React components have a lifecycle. With functional components, `useEffect` handles it all.

```
Mount   → component appears in DOM
Update  → state or props change, component re-renders
Unmount → component removed from DOM
```

```jsx
useEffect(() => {
  console.log("Mounted"); // runs on mount

  return () => {
    console.log("Unmounted"); // runs on unmount
  };
}, []);
```

---

## useRef

`useRef` gives you a mutable object that persists across renders without triggering a re-render. Commonly used to access DOM elements directly.

```jsx
import { useRef } from "react";

function InputFocus() {
  const inputRef = useRef(null);

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </div>
  );
}
```

Also used to store a previous value without causing a re-render:

```jsx
const prevCount = useRef(count);
useEffect(() => {
  prevCount.current = count;
});
```

---

## useContext — Global State Without Prop Drilling

Context lets you pass data deep into the component tree without threading props through every level.

```jsx
import { createContext, useContext, useState } from "react";

// 1. Create context
const ThemeContext = createContext("light");

// 2. Provide it at the top
function App() {
  const [theme, setTheme] = useState("dark");
  return (
    <ThemeContext.Provider value={theme}>
      <Page />
    </ThemeContext.Provider>
  );
}

// 3. Consume anywhere in the tree
function Button() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Click</button>;
}
```

---

## useMemo and useCallback — Performance

**`useMemo`** caches a computed value so it's not recalculated on every render.

```jsx
import { useMemo } from "react";

function ExpensiveList({ items, filter }) {
  const filtered = useMemo(
    () => items.filter((i) => i.includes(filter)),
    [items, filter], // recompute only when these change
  );
  return (
    <ul>
      {filtered.map((i) => (
        <li key={i}>{i}</li>
      ))}
    </ul>
  );
}
```

**`useCallback`** caches a function reference so it doesn't change on every render (useful when passing functions to child components).

```jsx
import { useCallback } from "react";

function Parent() {
  const handleClick = useCallback(() => {
    console.log("clicked");
  }, []); // stable reference

  return <Child onClick={handleClick} />;
}
```

---

## Conditional Rendering

```jsx
function Alert({ isLoggedIn }) {
  return (
    <div>
      {isLoggedIn ? <p>Welcome back!</p> : <p>Please log in.</p>}
      {isLoggedIn && <button>Logout</button>}
    </div>
  );
}
```

---

## Lists and Keys

When rendering arrays, each item needs a unique `key` prop. React uses keys to identify which items changed.

```jsx
const tasks = ["Code", "Review", "Deploy"];

function TaskList() {
  return (
    <ul>
      {tasks.map((task, index) => (
        <li key={index}>{task}</li> // prefer stable IDs over index
      ))}
    </ul>
  );
}
```

**Always prefer a stable unique ID as the key** (e.g., `task.id`), not array index, because index-based keys can cause bugs when the list reorders.

---

## React Reconciliation (Fiber)

**React Fiber** is the internal reconciliation engine (rewritten in React 16).

How it works:

1. A state change triggers a **render phase** — React calls your component functions and builds a new Fiber tree (all in memory, no DOM changes)
2. React diffs the new Fiber tree against the current one
3. In the **commit phase**, React applies the computed changes to the real DOM

Fiber allows React to:

- Pause and resume rendering work
- Prioritize urgent updates (user input) over less urgent ones (data fetching)
- This is the foundation of **Concurrent Mode**

---

## Key Feature Summary

| Feature                | What it does                               |
| ---------------------- | ------------------------------------------ |
| Virtual DOM            | Minimizes real DOM updates via diffing     |
| JSX                    | HTML-like syntax compiled to JS            |
| Components             | Reusable, isolated UI units                |
| Props                  | One-way data flow from parent to child     |
| State (`useState`)     | Reactive data inside a component           |
| Effects (`useEffect`)  | Side effects tied to render lifecycle      |
| Context (`useContext`) | Global state without prop drilling         |
| Refs (`useRef`)        | DOM access and persistent values           |
| Memoization            | Skip re-renders for unchanged data         |
| Fiber                  | Concurrent, interruptible rendering engine |

---

## Mental Model

```
User Action
    ↓
State changes (setState)
    ↓
React re-renders component (calls the function again)
    ↓
New VDOM produced
    ↓
Fiber diffs old VDOM vs new VDOM
    ↓
Minimal DOM update committed
    ↓
Browser paints the change
```

React is just a **state → UI** machine. Give it state, it figures out the DOM.
