# 动画效果

## 基础动效

- 按钮hover/点击反馈
- 页面加载动画
- 列表滚动效果
- Loading动画

### 基础动效代码

```css
/* 淡入动画 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 缩放动画 */
@keyframes scaleBounce {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

/* 旋转动画 */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

## 过渡动效

- 页面切换过渡
- 元素淡入淡出
- 滑动展开/收起
- 点击区域放大到全屏
- 页面转场动画

### 过渡动效代码

```css
/* 按钮悬停效果 */
.button {
  transition: all 0.2s ease-out;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* 输入框聚焦效果 */
.input-field {
  transition: all 0.2s ease;
}

.input-field:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}
```

## 高级动效

- 骨架屏加载
- 下拉刷新
- 滑动删除

### 高级动效代码

```css
/* 骨架屏加载 */
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s infinite;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```
