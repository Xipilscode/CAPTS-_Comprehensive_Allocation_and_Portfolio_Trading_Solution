{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 mkdir -p ~/.streamlit/
\f1\fs24 \
\

\f0\fs29\fsmilli14667 echo "\\
\f1\fs24 \

\f0\fs29\fsmilli14667 [general]\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 email = \\"your-email@domain.com\\"\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 " > ~/.streamlit/credentials.toml
\f1\fs24 \
\

\f0\fs29\fsmilli14667 echo "\\
\f1\fs24 \

\f0\fs29\fsmilli14667 [server]\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 headless = true\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 enableCORS=false\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 port = $PORT\\n\\
\f1\fs24 \

\f0\fs29\fsmilli14667 " > ~/.streamlit/config.toml
\f1\fs24 \
}