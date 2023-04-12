from dash import html
import feffery_antd_components as fac

from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '反馈'
                        },
                        {
                            'title': '自定义骨骼屏'
                        },
                        {
                            'title': 'AntdSkeletonButton 按钮占位图'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在自定义骨骼屏中构建按钮占位相关内容，'),
                        fac.AntdText('有关'),
                        fac.AntdText('AntdSkeletonButton', strong=True),
                        fac.AntdText('的使用示例请移步'),
                        fac.AntdText('AntdCustomSkeleton', strong=True),
                        fac.AntdText('对应的文档。')
                    ]
                )
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdSkeletonButton'
        )
    ],
    style={
        'display': 'flex'
    }
)
