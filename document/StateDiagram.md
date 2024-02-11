---
title: Serial Command Tool
---

```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> CUI_mode
    Still --> GUI_develop_mode
    Still --> GUI_user_mode
    Still --> GUI_admin_mode
    CUI_mode --> [*]
    GUI_develop_mode --> MainApplication
    GUI_user_mode --> MainApplication
    GUI_admin_mode --> MainApplication
    MainApplication --> [*]
```
